import twint

c = twint.Config()
c.Username = "SGeorgelondon"
c.Since = "2020-9-1"
c.Store_csv = True
c.Retweets = True
c.Images = 1==1
c.Output = "none"

twint.run.Search(c)