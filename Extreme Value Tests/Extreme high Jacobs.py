from ema_workbench import (TimeSeriesOutcome, perform_experiments, RealParameter, ema_logging, save_results, load_results, MultiprocessingEvaluator)
from ema_workbench.analysis import lines, Density, pairs_plotting, plotting
from ema_workbench.connectors.vensim import VensimModel

import matplotlib.gridspec as gridspec
from scipy.stats import gaussian_kde
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from sklearn.cluster import KMeans

def format_real_parameter(full_name, initial_value):
    lower = initial_value * 10
    upper = initial_value * 11
    return f"RealParameter('{full_name}', {lower}, {upper}),"

# Load Excel file — no headers
df = pd.read_excel('C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/change1 Jacobs.xlsx', header=None)

# Loop through rows
for index, row in df.iterrows():
    name = str(row[0]).strip()
    try:
        value = float(row[1])
        output = format_real_parameter(name, value)
        print(output)
    except ValueError:
        print(f"Invalid number at row {index + 1}: {row[1]}")


sector_names = ['Pharmaceutical Industry',
        'Chemical industry',
        'Automotive industry',
        'ICT information and services',
        'Aerospace construction and engineering',
        'Specialistic Technical and scientific activities',
        'Manufacturing of measurement instruments of navigation and watchmaking',
        'Editing audiovisual and diffusion',
        'Manufacturing of communication equipment',
        'Production and distribution of gas vapour and AC']

if __name__ == "__main__":
    # turn on logging
    ema_logging.log_to_stderr(ema_logging.INFO)
    wd = r'OneDrive - Delft University of Technology/Master Thesis'

    model = VensimModel("MARModel", wd=wd, model_file=r'RECOVERED_Simple model 4.vpmx')


    model.uncertainties = [
RealParameter('Attrition rate in sector[Pharmaceutical Industry]', 0.3700000047683716, 0.40700000524520874),
RealParameter('Attrition rate in sector[Chemical industry]', 0.2500000037252903, 0.27500000409781933),
RealParameter('Attrition rate in sector[Automotive industry]', 0.2999999932944775, 0.32999999262392526),
RealParameter('Attrition rate in sector[ICT information and services]', 0.1579999923706055, 0.17379999160766604),
RealParameter('Attrition rate in sector[Aerospace construction and engineering]', 0.2500000037252903, 0.27500000409781933),
RealParameter('Attrition rate in sector[Specialistic Technical and scientific activities]', 0.2500000037252903, 0.27500000409781933),
RealParameter('Attrition rate in sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.2500000037252903, 0.27500000409781933),
RealParameter('Attrition rate in sector[Editing audiovisual and diffusion]', 0.99, 1),
RealParameter('Attrition rate in sector[Manufacturing of communication equipment]', 0.2500000037252903, 0.27500000409781933),
RealParameter('Attrition rate in sector[Production and distribution of gas vapour and AC]', 0.2500000037252903, 0.27500000409781933),
RealParameter('Average mortality per age[Zeroto17]', 0.04000000189989805, 0.04400000208988786),
RealParameter('Average mortality per age[Eighteento24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[twentyfiveto45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[fortyfiveto65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Above65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Health18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Chemistry18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Process Engineering18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Audiovisual18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Multidisciplinary Sciences18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Digital18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Industry18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Mechanics18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Physics18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Information and communication studies18to24]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Health25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Chemistry25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Process Engineering25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Audiovisual25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Multidisciplinary Sciences25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Digital25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Industry25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Mechanics25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Physics25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Information and communication studies25to45]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Health45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Chemistry45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Process Engineering45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Audiovisual45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Multidisciplinary Sciences45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Digital45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Industry45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Mechanics45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Physics45to65]', 0.02000000094994903, 0.022000001044943932),
RealParameter('Average mortality per age[Information and communication studies45to65]', 0.3999999910593033, 0.4399999901652336),
RealParameter('Average Time to Market in Sector[Pharmaceutical Industry]', 120.0, 132.0),
RealParameter('Average Time to Market in Sector[Chemical industry]', 100.0, 110.0),
RealParameter('Average Time to Market in Sector[Automotive industry]', 60.0, 66.0),
RealParameter('Average Time to Market in Sector[ICT information and services]', 20.0, 22.0),
RealParameter('Average Time to Market in Sector[Aerospace construction and engineering]', 150.0, 165.0),
RealParameter('Average Time to Market in Sector[Specialistic Technical and scientific activities]', 50.0, 55.0),
RealParameter('Average Time to Market in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 50.0, 55.0),
RealParameter('Average Time to Market in Sector[Editing audiovisual and diffusion]', 20.0, 22.0),
RealParameter('Average Time to Market in Sector[Manufacturing of communication equipment]', 40.0, 44.0),
RealParameter('Average Time to Market in Sector[Production and distribution of gas vapour and AC]', 30.0, 33.0),
RealParameter('External investments', 100000.0, 110000.0),
RealParameter('"Government funding for public R&D in sector"', 8000000000.0, 8800000000.0),
RealParameter('Hiring and training time of employees', 20.0, 22.0),
RealParameter('Initial Added Value in Sector[Pharmaceutical Industry]', 26000000000.0, 28600000000.0),
RealParameter('Initial Added Value in Sector[Chemical industry]', 34000000000.0, 37400000000.0),
RealParameter('Initial Added Value in Sector[Automotive industry]', 108800000000.0, 119680000000.0),
RealParameter('Initial Added Value in Sector[ICT information and services]', 210800005120.0, 231880005632.0),
RealParameter('Initial Added Value in Sector[Aerospace construction and engineering]', 14000000000.0, 15400000000.0),
RealParameter('Initial Added Value in Sector[Specialistic Technical and scientific activities]', 26000000000.0, 28600000000.0),
RealParameter('Initial Added Value in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 20000000000.0, 22000000000.0),
RealParameter('Initial Added Value in Sector[Editing audiovisual and diffusion]', 43000002560.0, 47300002816.0),
RealParameter('Initial Added Value in Sector[Manufacturing of communication equipment]', 14000000000.0, 15400000000.0),
RealParameter('Initial Added Value in Sector[Production and distribution of gas vapour and AC]', 55000002560.0, 60500002816.0),
RealParameter('"Initial Employed R&D Workforce in Sector"[Pharmaceutical Industry]', 48805.2001953125, 53685.72021484375),
RealParameter('"Initial Employed R&D Workforce in Sector"[Chemical industry]', 21434.29931640625, 23577.729248046875),
RealParameter('"Initial Employed R&D Workforce in Sector"[Automotive industry]', 101620.0, 111782.0),
RealParameter('"Initial Employed R&D Workforce in Sector"[ICT information and services]', 115805.99609375, 127386.595703125),
RealParameter('"Initial Employed R&D Workforce in Sector"[Aerospace construction and engineering]', 46460.0, 51106.0),
RealParameter('"Initial Employed R&D Workforce in Sector"[Specialistic Technical and scientific activities]', 63527.2998046875, 69880.02978515625),
RealParameter('"Initial Employed R&D Workforce in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 57280.0, 63008.0),
RealParameter('"Initial Employed R&D Workforce in Sector"[Editing audiovisual and diffusion]', 52500.0, 57750.0),
RealParameter('"Initial Employed R&D Workforce in Sector"[Manufacturing of communication equipment]', 49730.0, 54703.0),
RealParameter('"Initial Employed R&D Workforce in Sector"[Production and distribution of gas vapour and AC]', 20050.0, 22055.0),
RealParameter('Initial knowledge specialisation in Sector[Pharmaceutical Industry]', 34900.0, 38390.0),
RealParameter('Initial knowledge specialisation in Sector[Chemical industry]', 4300.0, 4730.0),
RealParameter('Initial knowledge specialisation in Sector[Automotive industry]', 159510.0, 175461.0),
RealParameter('Initial knowledge specialisation in Sector[ICT information and services]', 7100.0, 7810.0),
RealParameter('Initial knowledge specialisation in Sector[Aerospace construction and engineering]', 2300.0, 2530.0),
RealParameter('Initial knowledge specialisation in Sector[Specialistic Technical and scientific activities]', 63100.0, 69410.0),
RealParameter('Initial knowledge specialisation in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 12100.0, 13310.0),
RealParameter('Initial knowledge specialisation in Sector[Editing audiovisual and diffusion]', 47300.0, 52030.0),
RealParameter('Initial knowledge specialisation in Sector[Manufacturing of communication equipment]', 8110.0, 8921.0),
RealParameter('Initial knowledge specialisation in Sector[Production and distribution of gas vapour and AC]', 4910.0, 5401.0),
RealParameter('Initial Population[Zeroto17]', 29113800.0, 32025180.0),
RealParameter('Initial Population[Eighteento24]', 11399400.0, 12539340.0),
RealParameter('Initial Population[twentyfiveto45]', 52596900.0, 57856590.0),
RealParameter('Initial Population[fortyfiveto65]', 17708200.0, 19479020.0),
RealParameter('Initial Population[Above65]', 25616800.0, 28178480.0),
RealParameter('Initial Population[Health18to24]', 253230.0, 278553.0),
RealParameter('Initial Population[Chemistry18to24]', 61710.0, 67881.0),
RealParameter('Initial Population[Process Engineering18to24]', 6320.0, 6952.0),
RealParameter('Initial Population[Audiovisual18to24]', 655970.0, 721567.0),
RealParameter('Initial Population[Multidisciplinary Sciences18to24]', 39930.0, 43923.0),
RealParameter('Initial Population[Digital18to24]', 118910.0, 130801.0),
RealParameter('Initial Population[Industry18to24]', 449760.0, 494736.0),
RealParameter('Initial Population[Mechanics18to24]', 38820.0, 42702.0),
RealParameter('Initial Population[Physics18to24]', 75880.0, 83468.0),
RealParameter('Initial Population[Information and communication studies18to24]', 73440.0, 80784.0),
RealParameter('Initial Population[Health25to45]', 90900.0, 99990.0),
RealParameter('Initial Population[Chemistry25to45]', 20370.0, 22407.0),
RealParameter('Initial Population[Process Engineering25to45]', 6700.0, 7370.0),
RealParameter('Initial Population[Audiovisual25to45]', 158650.0, 174515.0),
RealParameter('Initial Population[Multidisciplinary Sciences25to45]', 13200.0, 14520.0),
RealParameter('Initial Population[Digital25to45]', 117650.0, 129415.0),
RealParameter('Initial Population[Industry25to45]', 579390.0, 637329.0),
RealParameter('Initial Population[Mechanics25to45]', 22950.0, 25245.0),
RealParameter('Initial Population[Physics25to45]', 29200.0, 32120.0),
RealParameter('Initial Population[Information and communication studies25to45]', 58900.0, 64790.0),
RealParameter('Initial Population[Health45to65]', 90900.0, 99990.0),
RealParameter('Initial Population[Chemistry45to65]', 20370.0, 22407.0),
RealParameter('Initial Population[Process Engineering45to65]', 6700.0, 7370.0),
RealParameter('Initial Population[Audiovisual45to65]', 158650.0, 174515.0),
RealParameter('Initial Population[Multidisciplinary Sciences45to65]', 13200.0, 14520.0),
RealParameter('Initial Population[Digital45to65]', 117650.0, 129415.0),
RealParameter('Initial Population[Industry45to65]', 579390.0, 637329.0),
RealParameter('Initial Population[Mechanics45to65]', 22950.0, 25245.0),
RealParameter('Initial Population[Physics45to65]', 29200.0, 32120.0),
RealParameter('Initial Population[Information and communication studies45to65]', 58900.0, 64790.0),
RealParameter('Knowledge obsolescence time', 100.0, 110.0),
RealParameter('Percentage of adults enrolling in studies[Health18to24]', 0.01251820009201765, 0.013770020101219416),
RealParameter('Percentage of adults enrolling in studies[Chemistry18to24]', 0.005605570040643215, 0.006166127044707537),
RealParameter('Percentage of adults enrolling in studies[Process Engineering18to24]', 0.0007105700206011534, 0.0007816270226612687),
RealParameter('Percentage of adults enrolling in studies[Audiovisual18to24]', 0.01737809972837567, 0.019115909701213237),
RealParameter('Percentage of adults enrolling in studies[Multidisciplinary Sciences18to24]', 0.015623699873685839, 0.017186069861054424),
RealParameter('Percentage of adults enrolling in studies[Digital18to24]', 0.01805359963327646, 0.019858959596604105),
RealParameter('Percentage of adults enrolling in studies[Industry18to24]', 0.05575750023126602, 0.061333250254392624),
RealParameter('Percentage of adults enrolling in studies[Mechanics18to24]', 0.004237079992890358, 0.004660787992179394),
RealParameter('Percentage of adults enrolling in studies[Physics18to24]', 0.007140749949030578, 0.007854824943933636),
RealParameter('Percentage of adults enrolling in studies[Information and communication studies18to24]', 0.008886459982022643, 0.009775105980224907),
RealParameter('Percentage of innovative SMEs collaborating with others', 0.99, 1),
RealParameter('Percentage of profit from revenue in Sector[Pharmaceutical Industry]', 0.99, 1),
RealParameter('Percentage of profit from revenue in Sector[Chemical industry]', 0.99, 1),
RealParameter('Percentage of profit from revenue in Sector[Automotive industry]', 0.99, 1),
RealParameter('Percentage of profit from revenue in Sector[ICT information and services]', 0.99, 1),
RealParameter('Percentage of profit from revenue in Sector[Aerospace construction and engineering]', 0.99, 1),      
RealParameter('Percentage of profit from revenue in Sector[Specialistic Technical and scientific activities]', 0.99, 1),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.99, 1),
RealParameter('Percentage of profit from revenue in Sector[Editing audiovisual and diffusion]', 0.99, 1),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of communication equipment]', 0.99, 1),    
RealParameter('Percentage of profit from revenue in Sector[Production and distribution of gas vapour and AC]', 0.99, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Pharmaceutical Industry]', 0.99, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Chemical industry]', 0.99, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Automotive industry]', 0.99, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[ICT information and services]', 0.6539999693632126, 0.7193999662995338),       
RealParameter('"Percentage of R&D budget on total budget in Sector"[Aerospace construction and engineering]', 0.99, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Specialistic Technical and scientific activities]', 0.99, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.99, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Editing audiovisual and diffusion]', 0.99, 1),   
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of communication equipment]', 0.99, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Production and distribution of gas vapour and AC]', 0.7649999856948853, 0.8414999842643738),
RealParameter('Percentage of workforce wanting to go the private sector', 0.99, 1),
RealParameter('"Percentage of workforce wanting to go to R&D"', 0.99, 1),
RealParameter('"Public Funding for Private R&D in Sector"[Pharmaceutical Industry]', 0.1370000001043081, 0.1507000001147389),
RealParameter('"Public Funding for Private R&D in Sector"[Chemical industry]', 0.3629999980330467, 0.3992999978363514),
RealParameter('"Public Funding for Private R&D in Sector"[Automotive industry]', 0.08299999870359898, 0.09129999857395887),
RealParameter('"Public Funding for Private R&D in Sector"[ICT information and services]', 0.47699999064207077, 0.5246999897062778),
RealParameter('"Public Funding for Private R&D in Sector"[Aerospace construction and engineering]', 2.709000110626221, 2.979900121688843),
RealParameter('"Public Funding for Private R&D in Sector"[Specialistic Technical and scientific activities]', 1.068999990820885, 1.1758999899029734),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 2.113000005483627, 2.3243000060319896),
RealParameter('"Public Funding for Private R&D in Sector"[Editing audiovisual and diffusion]', 0.40199998766183853, 0.4421999864280224),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of communication equipment]', 2.587000131607056, 2.8457001447677617),      
RealParameter('"Public Funding for Private R&D in Sector"[Production and distribution of gas vapour and AC]', 0.1740000024437904, 0.19140000268816945),
RealParameter('"Public R&D expenditure per personel"[Pharmaceutical Industry]', 3341280.0, 3675408.0),
RealParameter('"Public R&D expenditure per personel"[Chemical industry]', 405231.015625, 445754.1171875),
RealParameter('"Public R&D expenditure per personel"[Automotive industry]', 1037780.0, 1141558.0),
RealParameter('"Public R&D expenditure per personel"[ICT information and services]', 1424970.0, 1567467.0),
RealParameter('"Public R&D expenditure per personel"[Aerospace construction and engineering]', 3936040.0, 4329644.0),
RealParameter('"Public R&D expenditure per personel"[Specialistic Technical and scientific activities]', 12927500.0, 14220250.0),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of measurement instruments of navigation and watchmaking]', 1276340.0, 1403974.0),
RealParameter('"Public R&D expenditure per personel"[Editing audiovisual and diffusion]', 405231.015625, 445754.1171875),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of communication equipment]', 405231.015625, 445754.1171875),
RealParameter('"Public R&D expenditure per personel"[Production and distribution of gas vapour and AC]', 405231.015625, 445754.1171875),
RealParameter('"Public-private collaboration per academic"[Pharmaceutical Industry]', 0.9000000357627869, 0.9900000393390656),
RealParameter('"Public-private collaboration per academic"[Chemical industry]', 0.9000000357627869, 0.9900000393390656),
RealParameter('"Public-private collaboration per academic"[Automotive industry]', 0.9000000357627869, 0.9900000393390656),
RealParameter('"Public-private collaboration per academic"[ICT information and services]', 0.9000000357627869, 0.9900000393390656),
RealParameter('"Public-private collaboration per academic"[Aerospace construction and engineering]', 0.9000000357627869, 0.9900000393390656),      
RealParameter('"Public-private collaboration per academic"[Specialistic Technical and scientific activities]', 0.9000000357627869, 0.9900000393390656),
RealParameter('"Public-private collaboration per academic"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.9000000357627869, 0.9900000393390656),
RealParameter('"Public-private collaboration per academic"[Editing audiovisual and diffusion]', 0.9000000357627869, 0.9900000393390656),
RealParameter('"Public-private collaboration per academic"[Manufacturing of communication equipment]', 0.9000000357627869, 0.9900000393390656),    
RealParameter('"Public-private collaboration per academic"[Production and distribution of gas vapour and AC]', 0.9000000357627869, 0.9900000393390656),
RealParameter('Relative share women in fertile age', 5.0, 5.5)
]

    model.outcomes = [
        TimeSeriesOutcome(f'Industry knowledge size[{s}]') for s in sector_names
    ] + [
        TimeSeriesOutcome(f'Workforce employed in knowledge intensive activities[{s}]') for s in sector_names
    ]

    results = perform_experiments(model, 2000)
    save_results(results, "./Extreme High values Jacobs.tar.gz")

    experiments, outcomes = results
