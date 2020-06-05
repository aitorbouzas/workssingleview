from fuzzywuzzy import fuzz

LEV_RATIO = 80


class GetWork:
    """
    GetWork for querying purposes
    """
    def __init__(self, work_repo, iswc_list):
        self.work_repo = work_repo
        self.iswc_list = iswc_list

    def execute(self):
        works = []
        for i in self.iswc_list:
            w = self.work_repo.first({'iswc': i})
            if w:
                works.append(w)
        return works


class PostWork:
    """
    PostWork will take into account if the work exists or not, in case it does it will call UpdateWork
    """
    def __init__(self, work_repo, provider_repo, data_dict):
        self.work_repo = work_repo
        self.provider_repo = provider_repo
        self.data_dict = data_dict

    def execute(self):
        work = self.work_repo.first({'iswc': self.data_dict.get('iswc')}) or self.work_repo.first({'title': self.data_dict.get('title')})
        if not work:
            providers = []
            if self.data_dict.get('providers'):
                providers = self.data_dict.get('providers')
                del self.data_dict['providers']

            work = self.work_repo.create(self.data_dict)

            for p in providers:
                provider = self.provider_repo.first({'name': p.get('source')})
                if not provider:
                    provider = self.provider_repo.create({'name': p.get('source')})

                work_provider_dict = {
                    'provider_id': provider.id,
                    'work_id': work.id,
                    'provider_reference': p.get('id'),
                }
                new_provider = self.work_repo.add_provider(work_provider_dict)
                new_provider['provider_name'] = provider.name
                work.add_provider(new_provider)
        else:
            update_work = UpdateWork(work.id, self.work_repo, self.provider_repo, self.data_dict)
            work = update_work.execute()
        return work


class UpdateWork:
    """
    UpdateWork contains the main reconciliation logic in which we check whether the Work has to be updated or not.
    Whether the Work is updated or not the provider will be added to the list
    """
    def __init__(self, work_id, work_repo, provider_repo, data_dict):
        self.work_id = work_id
        self.work_repo = work_repo
        self.provider_repo = provider_repo
        self.data_dict = data_dict

    def execute(self):
        work = self.work_repo.first({'id': self.work_id})
        update_dict = {}

        # ISWC only updated in case it is blank
        if 'iswc' in self.data_dict and not work.iswc:
            update_dict['iswc'] = self.data_dict.get('iswc')
            work.iswc = self.data_dict.get('iswc')

        # Contributors matching and reconciling
        contributors = work.contributors.split('|')
        for c in self.data_dict.get('contributors', '').split('|'):
            if c not in contributors:
                contributor = c

                # Check Levenshtein distance with all of them, stick to the longer in case they match
                changed = False
                for i, m in enumerate(contributors):
                    if fuzz.token_sort_ratio(c, m) >= LEV_RATIO or fuzz.partial_ratio(c, m) >= LEV_RATIO:
                        contributors[i] = c if len(c) > len(m) else m
                        changed = True
                        break

                if not changed:
                    contributors.append(contributor)

        if contributors != work.contributors.split('|'):
            update_dict['contributors'] = '|'.join(contributors)
            work.contributors = update_dict['contributors']

        # Add providers
        for p in self.data_dict.get('providers'):
            provider = self.provider_repo.first({'name': p.get('source')})
            if not provider:
                provider = self.provider_repo.create({'name': p.get('source')})

            if (provider.id, int(p.get('id'))) not in [(prov.provider_id, prov.provider_reference) for prov in work.providers]:
                work_provider_dict = {
                    'provider_id': provider.id,
                    'work_id': work.id,
                    'provider_reference': p.get('id'),
                }
                new_provider = self.work_repo.add_provider(work_provider_dict)
                new_provider['provider_name'] = provider.name
                work.add_provider(new_provider)

        self.work_repo.update(work.id, update_dict)

        return work
