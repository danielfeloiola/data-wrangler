# EXTRA
from scraper import main
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt


# bool to create a profile report
# creating the report can be slow
profile_report = False

# calls the main function to get the df
df = main()

# make a plot showing deaths per million and gdp per capita
df.plot(x='GDP per capita', y='Road deaths per Million Inhabitants', kind = 'scatter')
plt.savefig('extras/img1.png')

# make a plot showing deaths per million and vehicle ownership
df.plot(x='Vehicle ownership', y='Road deaths per Million Inhabitants', kind = 'scatter')
plt.savefig('extras/img2.png')


if profile_report:
    # generate a report using pandas profiling
    profile = ProfileReport(df,
                            title = "report",
                            samples=None,
                            missing_diagrams=None,
                            duplicates=None)

    # save it to a file
    profile.to_file(output_file = "extras/report.html")