import pandas as pd
class Module3:

    def search(self,searchTerm):
        df = pd.read_csv("/home/jaden/projects/socialMediaAnalytics/Module3/sample.csv",sep='\t',on_bad_lines='skip')
        entries = df.loc[df['description'].str.contains(searchTerm, case=False,na=False)]
        print(entries)
        return entries