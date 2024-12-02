class AccountRegistry:
        registry=[]

        @classmethod
        def add_account(cls, account):
            cls.registry.append(account)

        @classmethod 
        def get_accounts_count(cls):
            return len(cls.registry)
        @classmethod
        def search_by_pesel(cls, pesel):
            for i in cls.registry:
                  if i.pesel==pesel:
                    return i
            return None
        @classmethod
        def delete_by_pesel(cls, pesel):
            for konto in cls.registry:
                if konto.pesel == pesel:
                    cls.registry.remove(konto)
            return None