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

# def format_real_parameter(full_name, initial_value):
#     lower = initial_value * 0
#     upper = initial_value * 0.01
#     return f"RealParameter('{full_name}', {lower}, {upper}),"

# # Load Excel file — no headers
# df = pd.read_excel('C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/change1 Jacobs.xlsx', header=None)

# # Loop through rows
# for index, row in df.iterrows():
#     name = str(row[0]).strip()
#     try:
#         value = float(row[1])
#         output = format_real_parameter(name, value)
#         print(output)
#     except ValueError:
#         print(f"Invalid number at row {index + 1}: {row[1]}")


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


    model.uncertainties = [RealParameter('Attrition rate in sector[Pharmaceutical Industry]', 0.0, 0.00037000000476837156),
RealParameter('Attrition rate in sector[Chemical industry]', 0.0, 0.0002500000037252903),
RealParameter('Attrition rate in sector[Automotive industry]', 0.0, 0.0002999999932944775),
RealParameter('Attrition rate in sector[ICT information and services]', 0.0, 0.0001579999923706055),
RealParameter('Attrition rate in sector[Aerospace construction and engineering]', 0.0, 0.0002500000037252903),
RealParameter('Attrition rate in sector[Specialistic Technical and scientific activities]', 0.0, 0.0002500000037252903),
RealParameter('Attrition rate in sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.0002500000037252903),     
RealParameter('Attrition rate in sector[Editing audiovisual and diffusion]', 0.0, 0.002430000007152557),
RealParameter('Attrition rate in sector[Manufacturing of communication equipment]', 0.0, 0.0002500000037252903),
RealParameter('Attrition rate in sector[Production and distribution of gas vapour and AC]', 0.0, 0.0002500000037252903),
RealParameter('Average mortality per age[Zeroto17]', 0.0, 4.0000001899898055e-05),
RealParameter('Average mortality per age[Eighteento24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[twentyfiveto45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[fortyfiveto65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Above65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Health18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Chemistry18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Process Engineering18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Audiovisual18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Multidisciplinary Sciences18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Digital18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Industry18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Mechanics18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Physics18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Information and communication studies18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Health25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Chemistry25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Process Engineering25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Audiovisual25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Multidisciplinary Sciences25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Digital25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Industry25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Mechanics25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Physics25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Information and communication studies25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Health45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Chemistry45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Process Engineering45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Audiovisual45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Multidisciplinary Sciences45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Digital45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Industry45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Mechanics45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Physics45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Information and communication studies45to65]', 0.0, 0.0003999999910593033),
RealParameter('Average Time to Market in Sector[Pharmaceutical Industry]', 0.0, 0.12),
RealParameter('Average Time to Market in Sector[Chemical industry]', 0.0, 0.1),
RealParameter('Average Time to Market in Sector[Automotive industry]', 0.0, 0.06),
RealParameter('Average Time to Market in Sector[ICT information and services]', 0.0, 0.02),
RealParameter('Average Time to Market in Sector[Aerospace construction and engineering]', 0.0, 0.15),
RealParameter('Average Time to Market in Sector[Specialistic Technical and scientific activities]', 0.0, 0.05),
RealParameter('Average Time to Market in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.05),
RealParameter('Average Time to Market in Sector[Editing audiovisual and diffusion]', 0.0, 0.02),
RealParameter('Average Time to Market in Sector[Manufacturing of communication equipment]', 0.0, 0.04),
RealParameter('Average Time to Market in Sector[Production and distribution of gas vapour and AC]', 0.0, 0.03),
RealParameter('External investments', 0.0, 100.0),
RealParameter('"Government funding for public R&D in sector"', 0.0, 8000000.0),
RealParameter('Hiring and training time of employees', 0.0, 0.02),
RealParameter('Initial Added Value in Sector[Pharmaceutical Industry]', 0.0, 26000000.0),
RealParameter('Initial Added Value in Sector[Chemical industry]', 0.0, 34000000.0),
RealParameter('Initial Added Value in Sector[Automotive industry]', 0.0, 108800000.0),
RealParameter('Initial Added Value in Sector[ICT information and services]', 0.0, 210800005.12),
RealParameter('Initial Added Value in Sector[Aerospace construction and engineering]', 0.0, 14000000.0),
RealParameter('Initial Added Value in Sector[Specialistic Technical and scientific activities]', 0.0, 26000000.0),
RealParameter('Initial Added Value in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 20000000.0),
RealParameter('Initial Added Value in Sector[Editing audiovisual and diffusion]', 0.0, 43000002.56),
RealParameter('Initial Added Value in Sector[Manufacturing of communication equipment]', 0.0, 14000000.0),
RealParameter('Initial Added Value in Sector[Production and distribution of gas vapour and AC]', 0.0, 55000002.56),
RealParameter('"Initial Employed R&D Workforce in Sector"[Pharmaceutical Industry]', 0.0, 48.8052001953125),
RealParameter('"Initial Employed R&D Workforce in Sector"[Chemical industry]', 0.0, 21.43429931640625),
RealParameter('"Initial Employed R&D Workforce in Sector"[Automotive industry]', 0.0, 101.62),
RealParameter('"Initial Employed R&D Workforce in Sector"[ICT information and services]', 0.0, 115.80599609375),
RealParameter('"Initial Employed R&D Workforce in Sector"[Aerospace construction and engineering]', 0.0, 46.46),
RealParameter('"Initial Employed R&D Workforce in Sector"[Specialistic Technical and scientific activities]', 0.0, 63.5272998046875),
RealParameter('"Initial Employed R&D Workforce in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 57.28),   
RealParameter('"Initial Employed R&D Workforce in Sector"[Editing audiovisual and diffusion]', 0.0, 52.5),
RealParameter('"Initial Employed R&D Workforce in Sector"[Manufacturing of communication equipment]', 0.0, 49.730000000000004),
RealParameter('"Initial Employed R&D Workforce in Sector"[Production and distribution of gas vapour and AC]', 0.0, 20.05),
RealParameter('Initial knowledge specialisation in Sector[Pharmaceutical Industry]', 0.0, 34.9),
RealParameter('Initial knowledge specialisation in Sector[Chemical industry]', 0.0, 4.3),
RealParameter('Initial knowledge specialisation in Sector[Automotive industry]', 0.0, 159.51),
RealParameter('Initial knowledge specialisation in Sector[ICT information and services]', 0.0, 7.1000000000000005),
RealParameter('Initial knowledge specialisation in Sector[Aerospace construction and engineering]', 0.0, 2.3000000000000003),
RealParameter('Initial knowledge specialisation in Sector[Specialistic Technical and scientific activities]', 0.0, 63.1),
RealParameter('Initial knowledge specialisation in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 12.1),    
RealParameter('Initial knowledge specialisation in Sector[Editing audiovisual and diffusion]', 0.0, 47.300000000000004),
RealParameter('Initial knowledge specialisation in Sector[Manufacturing of communication equipment]', 0.0, 8.11),
RealParameter('Initial knowledge specialisation in Sector[Production and distribution of gas vapour and AC]', 0.0, 4.91),
RealParameter('Initial Population[Zeroto17]', 0.0, 29113.8),
RealParameter('Initial Population[Eighteento24]', 0.0, 11399.4),
RealParameter('Initial Population[twentyfiveto45]', 0.0, 52596.9),
RealParameter('Initial Population[fortyfiveto65]', 0.0, 17708.2),
RealParameter('Initial Population[Above65]', 0.0, 25616.8),
RealParameter('Initial Population[Health18to24]', 0.0, 253.23000000000002),
RealParameter('Initial Population[Chemistry18to24]', 0.0, 61.71),
RealParameter('Initial Population[Process Engineering18to24]', 0.0, 6.32),
RealParameter('Initial Population[Audiovisual18to24]', 0.0, 655.97),
RealParameter('Initial Population[Multidisciplinary Sciences18to24]', 0.0, 39.93),
RealParameter('Initial Population[Digital18to24]', 0.0, 118.91),
RealParameter('Initial Population[Industry18to24]', 0.0, 449.76),
RealParameter('Initial Population[Mechanics18to24]', 0.0, 38.82),
RealParameter('Initial Population[Physics18to24]', 0.0, 75.88),
RealParameter('Initial Population[Information and communication studies18to24]', 0.0, 73.44),
RealParameter('Initial Population[Health25to45]', 0.0, 90.9),
RealParameter('Initial Population[Chemistry25to45]', 0.0, 20.37),
RealParameter('Initial Population[Process Engineering25to45]', 0.0, 6.7),
RealParameter('Initial Population[Audiovisual25to45]', 0.0, 158.65),
RealParameter('Initial Population[Multidisciplinary Sciences25to45]', 0.0, 13.200000000000001),
RealParameter('Initial Population[Digital25to45]', 0.0, 117.65),
RealParameter('Initial Population[Industry25to45]', 0.0, 579.39),
RealParameter('Initial Population[Mechanics25to45]', 0.0, 22.95),
RealParameter('Initial Population[Physics25to45]', 0.0, 29.2),
RealParameter('Initial Population[Information and communication studies25to45]', 0.0, 58.9),
RealParameter('Initial Population[Health45to65]', 0.0, 90.9),
RealParameter('Initial Population[Chemistry45to65]', 0.0, 20.37),
RealParameter('Initial Population[Process Engineering45to65]', 0.0, 6.7),
RealParameter('Initial Population[Audiovisual45to65]', 0.0, 158.65),
RealParameter('Initial Population[Multidisciplinary Sciences45to65]', 0.0, 13.200000000000001),
RealParameter('Initial Population[Digital45to65]', 0.0, 117.65),
RealParameter('Initial Population[Industry45to65]', 0.0, 579.39),
RealParameter('Initial Population[Mechanics45to65]', 0.0, 22.95),
RealParameter('Initial Population[Physics45to65]', 0.0, 29.2),
RealParameter('Initial Population[Information and communication studies45to65]', 0.0, 58.9),
RealParameter('Knowledge obsolescence time', 0.0, 0.1),
RealParameter('Percentage of adults enrolling in studies[Health18to24]', 0.0, 1.2518200092017651e-05),
RealParameter('Percentage of adults enrolling in studies[Chemistry18to24]', 0.0, 5.6055700406432156e-06),
RealParameter('Percentage of adults enrolling in studies[Process Engineering18to24]', 0.0, 7.105700206011534e-07),
RealParameter('Percentage of adults enrolling in studies[Audiovisual18to24]', 0.0, 1.737809972837567e-05),
RealParameter('Percentage of adults enrolling in studies[Multidisciplinary Sciences18to24]', 0.0, 1.562369987368584e-05),
RealParameter('Percentage of adults enrolling in studies[Digital18to24]', 0.0, 1.805359963327646e-05),
RealParameter('Percentage of adults enrolling in studies[Industry18to24]', 0.0, 5.5757500231266025e-05),
RealParameter('Percentage of adults enrolling in studies[Mechanics18to24]', 0.0, 4.237079992890358e-06),
RealParameter('Percentage of adults enrolling in studies[Physics18to24]', 0.0, 7.140749949030579e-06),
RealParameter('Percentage of adults enrolling in studies[Information and communication studies18to24]', 0.0, 8.886459982022643e-06),
RealParameter('Percentage of innovative SMEs collaborating with others', 0.0, 0.006129999756813049),
RealParameter('Percentage of profit from revenue in Sector[Pharmaceutical Industry]', 0.0, 0.004709999859333038),
RealParameter('Percentage of profit from revenue in Sector[Chemical industry]', 0.0, 0.004589999914169312),
RealParameter('Percentage of profit from revenue in Sector[Automotive industry]', 0.0, 0.004104999899864197),
RealParameter('Percentage of profit from revenue in Sector[ICT information and services]', 0.0, 0.004154999852180481),
RealParameter('Percentage of profit from revenue in Sector[Aerospace construction and engineering]', 0.0, 0.002750000059604645),
RealParameter('Percentage of profit from revenue in Sector[Specialistic Technical and scientific activities]', 0.0, 0.0031400001049041748),        
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.004370000064373016),
RealParameter('Percentage of profit from revenue in Sector[Editing audiovisual and diffusion]', 0.0, 0.004149999916553497),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of communication equipment]', 0.0, 0.002750000059604645),
RealParameter('Percentage of profit from revenue in Sector[Production and distribution of gas vapour and AC]', 0.0, 0.007910000085830688),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Pharmaceutical Industry]', 0.0, 0.003465000092983246),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Chemical industry]', 0.0, 0.0018410000205039982),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Automotive industry]', 0.0, 0.001981000006198883),
RealParameter('"Percentage of R&D budget on total budget in Sector"[ICT information and services]', 0.0, 0.0006539999693632126),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Aerospace construction and engineering]', 0.0, 0.009710000157356262),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Specialistic Technical and scientific activities]', 0.0, 0.003937999904155731),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.00238999992609024),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Editing audiovisual and diffusion]', 0.0, 0.0013220000267028813),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of communication equipment]', 0.0, 0.0032330000400543207),       
RealParameter('"Percentage of R&D budget on total budget in Sector"[Production and distribution of gas vapour and AC]', 0.0, 0.0007649999856948852),
RealParameter('Percentage of workforce wanting to go the private sector', 0.0, 0.006999999880790711),
RealParameter('"Percentage of workforce wanting to go to R&D"', 0.0, 0.004000000059604645),
RealParameter('"Public Funding for Private R&D in Sector"[Pharmaceutical Industry]', 0.0, 0.0001370000001043081),
RealParameter('"Public Funding for Private R&D in Sector"[Chemical industry]', 0.0, 0.00036299999803304675),
RealParameter('"Public Funding for Private R&D in Sector"[Automotive industry]', 0.0, 8.299999870359898e-05),
RealParameter('"Public Funding for Private R&D in Sector"[ICT information and services]', 0.0, 0.0004769999906420708),
RealParameter('"Public Funding for Private R&D in Sector"[Aerospace construction and engineering]', 0.0, 0.0027090001106262213),
RealParameter('"Public Funding for Private R&D in Sector"[Specialistic Technical and scientific activities]', 0.0, 0.001068999990820885),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.0021130000054836273),
RealParameter('"Public Funding for Private R&D in Sector"[Editing audiovisual and diffusion]', 0.0, 0.00040199998766183854),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of communication equipment]', 0.0, 0.0025870001316070563),
RealParameter('"Public Funding for Private R&D in Sector"[Production and distribution of gas vapour and AC]', 0.0, 0.0001740000024437904),
RealParameter('"Public R&D expenditure per personel"[Pharmaceutical Industry]', 0.0, 3341.28),
RealParameter('"Public R&D expenditure per personel"[Chemical industry]', 0.0, 405.231015625),
RealParameter('"Public R&D expenditure per personel"[Automotive industry]', 0.0, 1037.78),
RealParameter('"Public R&D expenditure per personel"[ICT information and services]', 0.0, 1424.97),
RealParameter('"Public R&D expenditure per personel"[Aerospace construction and engineering]', 0.0, 3936.04),
RealParameter('"Public R&D expenditure per personel"[Specialistic Technical and scientific activities]', 0.0, 12927.5),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 1276.34),      
RealParameter('"Public R&D expenditure per personel"[Editing audiovisual and diffusion]', 0.0, 405.231015625),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of communication equipment]', 0.0, 405.231015625),
RealParameter('"Public R&D expenditure per personel"[Production and distribution of gas vapour and AC]', 0.0, 405.231015625),
RealParameter('"Public-private collaboration per academic"[Pharmaceutical Industry]', 0.0, 0.0009000000357627869),
RealParameter('"Public-private collaboration per academic"[Chemical industry]', 0.0, 0.0009000000357627869),
RealParameter('"Public-private collaboration per academic"[Automotive industry]', 0.0, 0.0009000000357627869),
RealParameter('"Public-private collaboration per academic"[ICT information and services]', 0.0, 0.0009000000357627869),
RealParameter('"Public-private collaboration per academic"[Aerospace construction and engineering]', 0.0, 0.0009000000357627869),
RealParameter('"Public-private collaboration per academic"[Specialistic Technical and scientific activities]', 0.0, 0.0009000000357627869),        
RealParameter('"Public-private collaboration per academic"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.0009000000357627869),
RealParameter('"Public-private collaboration per academic"[Editing audiovisual and diffusion]', 0.0, 0.0009000000357627869),
RealParameter('"Public-private collaboration per academic"[Manufacturing of communication equipment]', 0.0, 0.0009000000357627869),
RealParameter('"Public-private collaboration per academic"[Production and distribution of gas vapour and AC]', 0.0, 0.0009000000357627869),        
RealParameter('Relative share women in fertile age', 0.0, 0.005)
]

    model.outcomes = [
        TimeSeriesOutcome(f'Industry knowledge size[{s}]') for s in sector_names
    ] + [
        TimeSeriesOutcome(f'Workforce employed in knowledge intensive activities[{s}]') for s in sector_names
    ]

    results = perform_experiments(model, 2000)
    save_results(results, "./Extreme Low values Jacobs.tar.gz")

    experiments, outcomes = results
