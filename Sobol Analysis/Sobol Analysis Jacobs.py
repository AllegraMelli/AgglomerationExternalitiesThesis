from SALib.analyze import sobol
from ema_workbench.em_framework.salib_samplers import get_SALib_problem
from ema_workbench import (Samplers, TimeSeriesOutcome, perform_experiments, RealParameter, ema_logging, MultiprocessingEvaluator, save_results)
from ema_workbench.analysis import Density, pairs_plotting, plotting
from ema_workbench.connectors.vensim import VensimModel
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# def format_real_parameter(full_name, initial_value):
#     lower = initial_value * 0.8
#     upper = initial_value * 1.2
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

if __name__ == "__main__":
    # turn on logging
    ema_logging.log_to_stderr(ema_logging.INFO)
    wd = r'OneDrive - Delft University of Technology/Master Thesis'

    model = VensimModel("JacobsModel", wd=wd, model_file=r'RECOVERED_Simple model 4.vpmx')

    model.uncertainties = [RealParameter('Attrition rate in sector[Pharmaceutical Industry]', 0.02960000038146973, 0.04440000057220459),
RealParameter('Attrition rate in sector[Chemical industry]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Automotive industry]', 0.0239999994635582, 0.0359999991953373),
RealParameter('Attrition rate in sector[ICT information and services]', 0.012639999389648441, 0.01895999908447266),
RealParameter('Attrition rate in sector[Aerospace construction and engineering]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Specialistic Technical and scientific activities]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Editing audiovisual and diffusion]', 0.19440000057220458, 0.29160000085830684),
RealParameter('Attrition rate in sector[Manufacturing of communication equipment]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Production and distribution of gas vapour and AC]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Average mortality per age[Zeroto17]', 0.003200000151991844, 0.004800000227987766),
RealParameter('Average mortality per age[Eighteento24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[twentyfiveto45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[fortyfiveto65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Above65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies45to65]', 0.031999999284744264, 0.04799999892711639),
RealParameter('Average Time to Market in Sector[Pharmaceutical Industry]', 9.600000000000001, 14.399999999999999),
RealParameter('Average Time to Market in Sector[Chemical industry]', 8.0, 12.0),
RealParameter('Average Time to Market in Sector[Automotive industry]', 4.800000000000001, 7.199999999999999),
RealParameter('Average Time to Market in Sector[ICT information and services]', 1.6, 2.4),
RealParameter('Average Time to Market in Sector[Aerospace construction and engineering]', 12.0, 18.0),
RealParameter('Average Time to Market in Sector[Specialistic Technical and scientific activities]', 4.0, 6.0),
RealParameter('Average Time to Market in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 4.0, 6.0),
RealParameter('Average Time to Market in Sector[Editing audiovisual and diffusion]', 1.6, 2.4),
RealParameter('Average Time to Market in Sector[Manufacturing of communication equipment]', 3.2, 4.8),
RealParameter('Average Time to Market in Sector[Production and distribution of gas vapour and AC]', 2.4000000000000004, 3.5999999999999996),       
RealParameter('External investments', 8000.0, 12000.0),
RealParameter('"Government funding for public R&D in sector"', 640000000.0, 960000000.0),
RealParameter('Hiring and training time of employees', 1.6, 2.4),
RealParameter('Knowledge obsolescence time', 8.0, 12.0),
RealParameter('Percentage of adults enrolling in studies[Health18to24]', 0.001001456007361412, 0.0015021840110421181),
RealParameter('Percentage of adults enrolling in studies[Chemistry18to24]', 0.00044844560325145726, 0.0006726684048771858),
RealParameter('Percentage of adults enrolling in studies[Process Engineering18to24]', 5.684560164809227e-05, 8.52684024721384e-05),
RealParameter('Percentage of adults enrolling in studies[Audiovisual18to24]', 0.0013902479782700536, 0.00208537196740508),
RealParameter('Percentage of adults enrolling in studies[Multidisciplinary Sciences18to24]', 0.0012498959898948672, 0.0018748439848423005),        
RealParameter('Percentage of adults enrolling in studies[Digital18to24]', 0.001444287970662117, 0.002166431955993175),
RealParameter('Percentage of adults enrolling in studies[Industry18to24]', 0.0044606000185012816, 0.006690900027751923),
RealParameter('Percentage of adults enrolling in studies[Mechanics18to24]', 0.00033896639943122866, 0.0005084495991468429),
RealParameter('Percentage of adults enrolling in studies[Physics18to24]', 0.0005712599959224463, 0.0008568899938836694),
RealParameter('Percentage of adults enrolling in studies[Information and communication studies18to24]', 0.0007109167985618115, 0.001066375197842717),
RealParameter('Percentage of innovative SMEs collaborating with others', 0.49039998054504397, 0.7355999708175659),
RealParameter('Percentage of profit from revenue in Sector[Pharmaceutical Industry]', 0.37679998874664306, 0.5651999831199646),
RealParameter('Percentage of profit from revenue in Sector[Chemical industry]', 0.367199993133545, 0.5507999897003174),
RealParameter('Percentage of profit from revenue in Sector[Automotive industry]', 0.3283999919891358, 0.4925999879837036),
RealParameter('Percentage of profit from revenue in Sector[ICT information and services]', 0.3323999881744385, 0.4985999822616577),
RealParameter('Percentage of profit from revenue in Sector[Aerospace construction and engineering]', 0.2200000047683716, 0.33000000715255734),     
RealParameter('Percentage of profit from revenue in Sector[Specialistic Technical and scientific activities]', 0.251200008392334, 0.376800012588501),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.3496000051498413, 0.5244000077247619),
RealParameter('Percentage of profit from revenue in Sector[Editing audiovisual and diffusion]', 0.33199999332427976, 0.4979999899864196),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of communication equipment]', 0.2200000047683716, 0.33000000715255734),   
RealParameter('Percentage of profit from revenue in Sector[Production and distribution of gas vapour and AC]', 0.6328000068664551, 0.9492000102996826),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Pharmaceutical Industry]', 0.2772000074386597, 0.4158000111579895),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Chemical industry]', 0.14728000164031985, 0.22092000246047977),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Automotive industry]', 0.15848000049591066, 0.23772000074386596),
RealParameter('"Percentage of R&D budget on total budget in Sector"[ICT information and services]', 0.05231999754905701, 0.0784799963235855),      
RealParameter('"Percentage of R&D budget on total budget in Sector"[Aerospace construction and engineering]', 0.7768000125885011, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Specialistic Technical and scientific activities]', 0.3150399923324585, 0.47255998849868774),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.19119999408721922, 0.28679999113082877),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Editing audiovisual and diffusion]', 0.10576000213623049, 0.15864000320434574),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of communication equipment]', 0.25864000320434566, 0.3879600048065185),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Production and distribution of gas vapour and AC]', 0.061199998855590826, 0.09179999828338622),
RealParameter('Percentage of workforce wanting to go the private sector', 0.5599999904632569, 0.8399999856948852),
RealParameter('"Percentage of workforce wanting to go to R&D"', 0.3200000047683716, 0.48000000715255736),
RealParameter('"Public Funding for Private R&D in Sector"[Pharmaceutical Industry]', 0.010960000008344649, 0.01644000001251697),
RealParameter('"Public Funding for Private R&D in Sector"[Chemical industry]', 0.02903999984264374, 0.04355999976396561),
RealParameter('"Public Funding for Private R&D in Sector"[Automotive industry]', 0.006639999896287919, 0.009959999844431877),
RealParameter('"Public Funding for Private R&D in Sector"[ICT information and services]', 0.038159999251365664, 0.05723999887704849),
RealParameter('"Public Funding for Private R&D in Sector"[Aerospace construction and engineering]', 0.2167200088500977, 0.3250800132751465),       
RealParameter('"Public Funding for Private R&D in Sector"[Specialistic Technical and scientific activities]', 0.0855199992656708, 0.1282799988985062),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.16904000043869016, 0.25356000065803525),
RealParameter('"Public Funding for Private R&D in Sector"[Editing audiovisual and diffusion]', 0.03215999901294708, 0.048239998519420624),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of communication equipment]', 0.2069600105285645, 0.31044001579284675),    
RealParameter('"Public Funding for Private R&D in Sector"[Production and distribution of gas vapour and AC]', 0.013920000195503233, 0.020880000293254847),
RealParameter('"Public R&D expenditure per personel"[Pharmaceutical Industry]', 267302.4, 400953.6),
RealParameter('"Public R&D expenditure per personel"[Chemical industry]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Automotive industry]', 83022.40000000001, 124533.59999999999),
RealParameter('"Public R&D expenditure per personel"[ICT information and services]', 113997.6, 170996.4),
RealParameter('"Public R&D expenditure per personel"[Aerospace construction and engineering]', 314883.2, 472324.8),
RealParameter('"Public R&D expenditure per personel"[Specialistic Technical and scientific activities]', 1034200.0, 1551300.0),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of measurement instruments of navigation and watchmaking]', 102107.20000000001, 153160.8),
RealParameter('"Public R&D expenditure per personel"[Editing audiovisual and diffusion]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of communication equipment]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Production and distribution of gas vapour and AC]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of communication equipment]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Production and distribution of gas vapour and AC]', 32418.48125, 48627.721874999996),
RealParameter('"Public-private collaboration per academic"[Pharmaceutical Industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Chemical industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Automotive industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[ICT information and services]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Aerospace construction and engineering]', 0.07200000286102295, 0.10800000429153442),    
RealParameter('"Public-private collaboration per academic"[Specialistic Technical and scientific activities]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Editing audiovisual and diffusion]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Manufacturing of communication equipment]', 0.07200000286102295, 0.10800000429153442),  
RealParameter('"Public-private collaboration per academic"[Production and distribution of gas vapour and AC]', 0.07200000286102295, 0.10800000429153442),
RealParameter('Relative share women in fertile age', 0.4, 0.6),
RealParameter('Relatedness[Pharmaceutical Industry,Chemical industry]', 0.23783760070800786, 0.3567564010620118),
RealParameter('Relatedness[Pharmaceutical Industry,Automotive industry]', 0.022222240269184113, 0.033333360403776165),
RealParameter('Relatedness[Pharmaceutical Industry,ICT information and services]', 0.06399999856948853, 0.09599999785423279),
RealParameter('Relatedness[Pharmaceutical Industry,Aerospace construction and engineering]', 0.07272728085517884, 0.10909092128276825),
RealParameter('Relatedness[Pharmaceutical Industry,Manufacturing of measurement instruments of navigation and watchmaking]', 0.06666663885116578, 0.09999995827674865),
RealParameter('Relatedness[Pharmaceutical Industry,Manufacturing of communication equipment]', 0.04210528135299683, 0.06315792202949523),
RealParameter('Relatedness[Chemical industry,Pharmaceutical Industry]', 0.23783760070800786, 0.3567564010620118),
RealParameter('Relatedness[Chemical industry,Automotive industry]', 0.022222240269184113, 0.033333360403776165),
RealParameter('Relatedness[Chemical industry,ICT information and services]', 0.03076919913291931, 0.04615379869937897),
RealParameter('Relatedness[Chemical industry,Aerospace construction and engineering]', 0.022857120633125307, 0.03428568094968796),
RealParameter('Relatedness[Chemical industry,Manufacturing of measurement instruments of navigation and watchmaking]', 0.06666663885116578, 0.09999995827674865),
RealParameter('Relatedness[Chemical industry,Manufacturing of communication equipment]', 0.04210528135299683, 0.06315792202949523),
RealParameter('Relatedness[Chemical industry,Production and distribution of gas vapour and AC]', 0.11034480333328248, 0.1655172049999237),
RealParameter('Relatedness[Automotive industry,Pharmaceutical Industry]', 0.022222240269184113, 0.033333360403776165),
RealParameter('Relatedness[Automotive industry,Chemical industry]', 0.022222240269184113, 0.033333360403776165),
RealParameter('Relatedness[Automotive industry,ICT information and services]', 0.03902440071105957, 0.05853660106658935),
RealParameter('Relatedness[Automotive industry,Aerospace construction and engineering]', 0.15238080024719242, 0.2285712003707886),
RealParameter('Relatedness[Automotive industry,Specialistic Technical and scientific activities]', 0.16842080354690553, 0.25263120532035827),      
RealParameter('Relatedness[Automotive industry,Manufacturing of measurement instruments of navigation and watchmaking]', 0.029629600048065186, 0.044444400072097774),
RealParameter('Relatedness[ICT information and services,Pharmaceutical Industry]', 0.06399999856948853, 0.09599999785423279),
RealParameter('Relatedness[ICT information and services,Chemical industry]', 0.03076919913291931, 0.04615379869937897),
RealParameter('Relatedness[ICT information and services,Automotive industry]', 0.03902440071105957, 0.05853660106658935),
RealParameter('Relatedness[ICT information and services,Aerospace construction and engineering]', 0.06153848171234131, 0.09230772256851195),       
RealParameter('Relatedness[ICT information and services,Specialistic Technical and scientific activities]', 0.020512799918651584, 0.030769199877977375),
RealParameter('Relatedness[ICT information and services,Manufacturing of measurement instruments of navigation and watchmaking]', 0.03720928132534027, 0.055813921988010405),
RealParameter('Relatedness[ICT information and services,Editing audiovisual and diffusion]', 0.25806479454040526, 0.3870971918106079),
RealParameter('Relatedness[ICT information and services,Manufacturing of communication equipment]', 0.12000000476837161, 0.1800000071525574),      
RealParameter('Relatedness[Aerospace construction and engineering,Pharmaceutical Industry]', 0.07272728085517884, 0.10909092128276825),
RealParameter('Relatedness[Aerospace construction and engineering,Chemical industry]', 0.022857120633125307, 0.03428568094968796),
RealParameter('Relatedness[Aerospace construction and engineering,Automotive industry]', 0.15238080024719242, 0.2285712003707886),
RealParameter('Relatedness[Aerospace construction and engineering,ICT information and services]', 0.06153848171234131, 0.09230772256851195),       
RealParameter('Relatedness[Aerospace construction and engineering,Specialistic Technical and scientific activities]', 0.0380952000617981, 0.05714280009269714),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Automotive industry]', 0.16842080354690553, 0.25263120532035827),      
RealParameter('Relatedness[Specialistic Technical and scientific activities,ICT information and services]', 0.020512799918651584, 0.030769199877977375),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Aerospace construction and engineering]', 0.0380952000617981, 0.05714280009269714),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Manufacturing of measurement instruments of navigation and watchmaking]', 0.033333361148834235, 0.05000004172325135),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Production and distribution of gas vapour and AC]', 0.15000000000000002, 0.22499999999999998),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Pharmaceutical Industry]', 0.06666663885116578, 0.09999995827674865),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Chemical industry]', 0.06666663885116578, 0.09999995827674865),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Automotive industry]', 0.029629600048065186, 0.044444400072097774),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,ICT information and services]', 0.03720928132534027, 0.055813921988010405),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Specialistic Technical and scientific activities]', 0.033333361148834235, 0.05000004172325135),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Manufacturing of communication equipment]', 0.11851840019226073, 0.17777760028839107),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Production and distribution of gas vapour and AC]', 0.034782639145851134, 0.052173958718776704),
RealParameter('Relatedness[Editing audiovisual and diffusion,ICT information and services]', 0.25806479454040526, 0.3870971918106079),
RealParameter('Relatedness[Editing audiovisual and diffusion,Manufacturing of communication equipment]', 0.03076919913291931, 0.04615379869937897),
RealParameter('Relatedness[Manufacturing of communication equipment,Pharmaceutical Industry]', 0.04210528135299683, 0.06315792202949523),
RealParameter('Relatedness[Manufacturing of communication equipment,Chemical industry]', 0.04210528135299683, 0.06315792202949523),
RealParameter('Relatedness[Manufacturing of communication equipment,ICT information and services]', 0.12000000476837161, 0.1800000071525574),   
RealParameter('Relatedness[Manufacturing of communication equipment,Manufacturing of measurement instruments of navigation and watchmaking]', 0.11851840019226073, 0.17777760028839107),
RealParameter('Relatedness[Manufacturing of communication equipment,Editing audiovisual and diffusion]', 0.03076919913291931, 0.04615379869937897),
RealParameter('Relatedness[Manufacturing of communication equipment,Production and distribution of gas vapour and AC]', 0.033333361148834235, 0.05000004172325135),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Chemical industry]', 0.11034480333328248, 0.1655172049999237),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Specialistic Technical and scientific activities]', 0.15000000000000002, 0.22499999999999998),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Manufacturing of measurement instruments of navigation and watchmaking]', 0.034782639145851134, 0.052173958718776704),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Manufacturing of communication equipment]', 0.033333361148834235, 0.05000004172325135)]

    
    model.levers = [RealParameter('Attrition rate in sector[Pharmaceutical Industry]', 0.02960000038146973, 0.04440000057220459),
RealParameter('Attrition rate in sector[Chemical industry]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Automotive industry]', 0.0239999994635582, 0.0359999991953373),
RealParameter('Attrition rate in sector[ICT information and services]', 0.012639999389648441, 0.01895999908447266),
RealParameter('Attrition rate in sector[Aerospace construction and engineering]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Specialistic Technical and scientific activities]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Editing audiovisual and diffusion]', 0.19440000057220458, 0.29160000085830684),
RealParameter('Attrition rate in sector[Manufacturing of communication equipment]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Production and distribution of gas vapour and AC]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Average mortality per age[Zeroto17]', 0.003200000151991844, 0.004800000227987766),
RealParameter('Average mortality per age[Eighteento24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[twentyfiveto45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[fortyfiveto65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Above65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies45to65]', 0.031999999284744264, 0.04799999892711639),
RealParameter('Average Time to Market in Sector[Pharmaceutical Industry]', 9.600000000000001, 14.399999999999999),
RealParameter('Average Time to Market in Sector[Chemical industry]', 8.0, 12.0),
RealParameter('Average Time to Market in Sector[Automotive industry]', 4.800000000000001, 7.199999999999999),
RealParameter('Average Time to Market in Sector[ICT information and services]', 1.6, 2.4),
RealParameter('Average Time to Market in Sector[Aerospace construction and engineering]', 12.0, 18.0),
RealParameter('Average Time to Market in Sector[Specialistic Technical and scientific activities]', 4.0, 6.0),
RealParameter('Average Time to Market in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 4.0, 6.0),
RealParameter('Average Time to Market in Sector[Editing audiovisual and diffusion]', 1.6, 2.4),
RealParameter('Average Time to Market in Sector[Manufacturing of communication equipment]', 3.2, 4.8),
RealParameter('Average Time to Market in Sector[Production and distribution of gas vapour and AC]', 2.4000000000000004, 3.5999999999999996),       
RealParameter('External investments', 8000.0, 12000.0),
RealParameter('"Government funding for public R&D in sector"', 640000000.0, 960000000.0),
RealParameter('Hiring and training time of employees', 1.6, 2.4),
RealParameter('Knowledge obsolescence time', 8.0, 12.0),
RealParameter('Percentage of adults enrolling in studies[Health18to24]', 0.001001456007361412, 0.0015021840110421181),
RealParameter('Percentage of adults enrolling in studies[Chemistry18to24]', 0.00044844560325145726, 0.0006726684048771858),
RealParameter('Percentage of adults enrolling in studies[Process Engineering18to24]', 5.684560164809227e-05, 8.52684024721384e-05),
RealParameter('Percentage of adults enrolling in studies[Audiovisual18to24]', 0.0013902479782700536, 0.00208537196740508),
RealParameter('Percentage of adults enrolling in studies[Multidisciplinary Sciences18to24]', 0.0012498959898948672, 0.0018748439848423005),        
RealParameter('Percentage of adults enrolling in studies[Digital18to24]', 0.001444287970662117, 0.002166431955993175),
RealParameter('Percentage of adults enrolling in studies[Industry18to24]', 0.0044606000185012816, 0.006690900027751923),
RealParameter('Percentage of adults enrolling in studies[Mechanics18to24]', 0.00033896639943122866, 0.0005084495991468429),
RealParameter('Percentage of adults enrolling in studies[Physics18to24]', 0.0005712599959224463, 0.0008568899938836694),
RealParameter('Percentage of adults enrolling in studies[Information and communication studies18to24]', 0.0007109167985618115, 0.001066375197842717),
RealParameter('Percentage of innovative SMEs collaborating with others', 0.49039998054504397, 0.7355999708175659),
RealParameter('Percentage of profit from revenue in Sector[Pharmaceutical Industry]', 0.37679998874664306, 0.5651999831199646),
RealParameter('Percentage of profit from revenue in Sector[Chemical industry]', 0.367199993133545, 0.5507999897003174),
RealParameter('Percentage of profit from revenue in Sector[Automotive industry]', 0.3283999919891358, 0.4925999879837036),
RealParameter('Percentage of profit from revenue in Sector[ICT information and services]', 0.3323999881744385, 0.4985999822616577),
RealParameter('Percentage of profit from revenue in Sector[Aerospace construction and engineering]', 0.2200000047683716, 0.33000000715255734),     
RealParameter('Percentage of profit from revenue in Sector[Specialistic Technical and scientific activities]', 0.251200008392334, 0.376800012588501),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.3496000051498413, 0.5244000077247619),
RealParameter('Percentage of profit from revenue in Sector[Editing audiovisual and diffusion]', 0.33199999332427976, 0.4979999899864196),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of communication equipment]', 0.2200000047683716, 0.33000000715255734),   
RealParameter('Percentage of profit from revenue in Sector[Production and distribution of gas vapour and AC]', 0.6328000068664551, 0.9492000102996826),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Pharmaceutical Industry]', 0.2772000074386597, 0.4158000111579895),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Chemical industry]', 0.14728000164031985, 0.22092000246047977),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Automotive industry]', 0.15848000049591066, 0.23772000074386596),
RealParameter('"Percentage of R&D budget on total budget in Sector"[ICT information and services]', 0.05231999754905701, 0.0784799963235855),      
RealParameter('"Percentage of R&D budget on total budget in Sector"[Aerospace construction and engineering]', 0.7768000125885011, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Specialistic Technical and scientific activities]', 0.3150399923324585, 0.47255998849868774),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.19119999408721922, 0.28679999113082877),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Editing audiovisual and diffusion]', 0.10576000213623049, 0.15864000320434574),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of communication equipment]', 0.25864000320434566, 0.3879600048065185),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Production and distribution of gas vapour and AC]', 0.061199998855590826, 0.09179999828338622),
RealParameter('Percentage of workforce wanting to go the private sector', 0.5599999904632569, 0.8399999856948852),
RealParameter('"Percentage of workforce wanting to go to R&D"', 0.3200000047683716, 0.48000000715255736),
RealParameter('"Public Funding for Private R&D in Sector"[Pharmaceutical Industry]', 0.010960000008344649, 0.01644000001251697),
RealParameter('"Public Funding for Private R&D in Sector"[Chemical industry]', 0.02903999984264374, 0.04355999976396561),
RealParameter('"Public Funding for Private R&D in Sector"[Automotive industry]', 0.006639999896287919, 0.009959999844431877),
RealParameter('"Public Funding for Private R&D in Sector"[ICT information and services]', 0.038159999251365664, 0.05723999887704849),
RealParameter('"Public Funding for Private R&D in Sector"[Aerospace construction and engineering]', 0.2167200088500977, 0.3250800132751465),       
RealParameter('"Public Funding for Private R&D in Sector"[Specialistic Technical and scientific activities]', 0.0855199992656708, 0.1282799988985062),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.16904000043869016, 0.25356000065803525),
RealParameter('"Public Funding for Private R&D in Sector"[Editing audiovisual and diffusion]', 0.03215999901294708, 0.048239998519420624),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of communication equipment]', 0.2069600105285645, 0.31044001579284675),    
RealParameter('"Public Funding for Private R&D in Sector"[Production and distribution of gas vapour and AC]', 0.013920000195503233, 0.020880000293254847),
RealParameter('"Public R&D expenditure per personel"[Pharmaceutical Industry]', 267302.4, 400953.6),
RealParameter('"Public R&D expenditure per personel"[Chemical industry]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Automotive industry]', 83022.40000000001, 124533.59999999999),
RealParameter('"Public R&D expenditure per personel"[ICT information and services]', 113997.6, 170996.4),
RealParameter('"Public R&D expenditure per personel"[Aerospace construction and engineering]', 314883.2, 472324.8),
RealParameter('"Public R&D expenditure per personel"[Specialistic Technical and scientific activities]', 1034200.0, 1551300.0),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of measurement instruments of navigation and watchmaking]', 102107.20000000001, 153160.8),
RealParameter('"Public R&D expenditure per personel"[Editing audiovisual and diffusion]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of communication equipment]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Production and distribution of gas vapour and AC]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Manufacturing of communication equipment]', 32418.48125, 48627.721874999996),
RealParameter('"Public R&D expenditure per personel"[Production and distribution of gas vapour and AC]', 32418.48125, 48627.721874999996),
RealParameter('"Public-private collaboration per academic"[Pharmaceutical Industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Chemical industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Automotive industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[ICT information and services]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Aerospace construction and engineering]', 0.07200000286102295, 0.10800000429153442),    
RealParameter('"Public-private collaboration per academic"[Specialistic Technical and scientific activities]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Editing audiovisual and diffusion]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Manufacturing of communication equipment]', 0.07200000286102295, 0.10800000429153442),  
RealParameter('"Public-private collaboration per academic"[Production and distribution of gas vapour and AC]', 0.07200000286102295, 0.10800000429153442),
RealParameter('Relative share women in fertile age', 0.4, 0.6),
RealParameter('Relatedness[Pharmaceutical Industry,Pharmaceutical Industry]', 0.0, 0.0),
RealParameter('Relatedness[Pharmaceutical Industry,Chemical industry]', 0.23783760070800786, 0.3567564010620118),
RealParameter('Relatedness[Pharmaceutical Industry,Automotive industry]', 0.022222240269184113, 0.033333360403776165),
RealParameter('Relatedness[Pharmaceutical Industry,ICT information and services]', 0.06399999856948853, 0.09599999785423279),
RealParameter('Relatedness[Pharmaceutical Industry,Aerospace construction and engineering]', 0.07272728085517884, 0.10909092128276825),
RealParameter('Relatedness[Pharmaceutical Industry,Specialistic Technical and scientific activities]', 0.0, 0.0),
RealParameter('Relatedness[Pharmaceutical Industry,Manufacturing of measurement instruments of navigation and watchmaking]', 0.06666663885116578, 0.09999995827674865),
RealParameter('Relatedness[Pharmaceutical Industry,Editing audiovisual and diffusion]', 0.0, 0.0),
RealParameter('Relatedness[Pharmaceutical Industry,Manufacturing of communication equipment]', 0.04210528135299683, 0.06315792202949523),
RealParameter('Relatedness[Pharmaceutical Industry,Production and distribution of gas vapour and AC]', 0.0, 0.0),
RealParameter('Relatedness[Chemical industry,Pharmaceutical Industry]', 0.23783760070800786, 0.3567564010620118),
RealParameter('Relatedness[Chemical industry,Chemical industry]', 0.0, 0.0),
RealParameter('Relatedness[Chemical industry,Automotive industry]', 0.022222240269184113, 0.033333360403776165),
RealParameter('Relatedness[Chemical industry,ICT information and services]', 0.03076919913291931, 0.04615379869937897),
RealParameter('Relatedness[Chemical industry,Aerospace construction and engineering]', 0.022857120633125307, 0.03428568094968796),
RealParameter('Relatedness[Chemical industry,Specialistic Technical and scientific activities]', 0.0, 0.0),
RealParameter('Relatedness[Chemical industry,Manufacturing of measurement instruments of navigation and watchmaking]', 0.06666663885116578, 0.09999995827674865),
RealParameter('Relatedness[Chemical industry,Editing audiovisual and diffusion]', 0.0, 0.0),
RealParameter('Relatedness[Chemical industry,Manufacturing of communication equipment]', 0.04210528135299683, 0.06315792202949523),
RealParameter('Relatedness[Chemical industry,Production and distribution of gas vapour and AC]', 0.11034480333328248, 0.1655172049999237),
RealParameter('Relatedness[Automotive industry,Pharmaceutical Industry]', 0.022222240269184113, 0.033333360403776165),
RealParameter('Relatedness[Automotive industry,Chemical industry]', 0.022222240269184113, 0.033333360403776165),
RealParameter('Relatedness[Automotive industry,Automotive industry]', 0.0, 0.0),
RealParameter('Relatedness[Automotive industry,ICT information and services]', 0.03902440071105957, 0.05853660106658935),
RealParameter('Relatedness[Automotive industry,Aerospace construction and engineering]', 0.15238080024719242, 0.2285712003707886),
RealParameter('Relatedness[Automotive industry,Specialistic Technical and scientific activities]', 0.16842080354690553, 0.25263120532035827),      
RealParameter('Relatedness[Automotive industry,Manufacturing of measurement instruments of navigation and watchmaking]', 0.029629600048065186, 0.044444400072097774),
RealParameter('Relatedness[Automotive industry,Editing audiovisual and diffusion]', 0.0, 0.0),
RealParameter('Relatedness[Automotive industry,Manufacturing of communication equipment]', 0.0, 0.0),
RealParameter('Relatedness[Automotive industry,Production and distribution of gas vapour and AC]', 0.0, 0.0),
RealParameter('Relatedness[ICT information and services,Pharmaceutical Industry]', 0.06399999856948853, 0.09599999785423279),
RealParameter('Relatedness[ICT information and services,Chemical industry]', 0.03076919913291931, 0.04615379869937897),
RealParameter('Relatedness[ICT information and services,Automotive industry]', 0.03902440071105957, 0.05853660106658935),
RealParameter('Relatedness[ICT information and services,ICT information and services]', 0.0, 0.0),
RealParameter('Relatedness[ICT information and services,Aerospace construction and engineering]', 0.06153848171234131, 0.09230772256851195),       
RealParameter('Relatedness[ICT information and services,Specialistic Technical and scientific activities]', 0.020512799918651584, 0.030769199877977375),
RealParameter('Relatedness[ICT information and services,Manufacturing of measurement instruments of navigation and watchmaking]', 0.03720928132534027, 0.055813921988010405),
RealParameter('Relatedness[ICT information and services,Editing audiovisual and diffusion]', 0.25806479454040526, 0.3870971918106079),
RealParameter('Relatedness[ICT information and services,Manufacturing of communication equipment]', 0.12000000476837161, 0.1800000071525574),      
RealParameter('Relatedness[ICT information and services,Production and distribution of gas vapour and AC]', 0.0, 0.0),
RealParameter('Relatedness[Aerospace construction and engineering,Pharmaceutical Industry]', 0.07272728085517884, 0.10909092128276825),
RealParameter('Relatedness[Aerospace construction and engineering,Chemical industry]', 0.022857120633125307, 0.03428568094968796),
RealParameter('Relatedness[Aerospace construction and engineering,Automotive industry]', 0.15238080024719242, 0.2285712003707886),
RealParameter('Relatedness[Aerospace construction and engineering,ICT information and services]', 0.06153848171234131, 0.09230772256851195),       
RealParameter('Relatedness[Aerospace construction and engineering,Aerospace construction and engineering]', 0.0, 0.0),
RealParameter('Relatedness[Aerospace construction and engineering,Specialistic Technical and scientific activities]', 0.0380952000617981, 0.05714280009269714),
RealParameter('Relatedness[Aerospace construction and engineering,Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.0),
RealParameter('Relatedness[Aerospace construction and engineering,Editing audiovisual and diffusion]', 0.0, 0.0),
RealParameter('Relatedness[Aerospace construction and engineering,Manufacturing of communication equipment]', 0.0, 0.0),
RealParameter('Relatedness[Aerospace construction and engineering,Production and distribution of gas vapour and AC]', 0.0, 0.0),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Pharmaceutical Industry]', 0.0, 0.0),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Chemical industry]', 0.0, 0.0),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Automotive industry]', 0.16842080354690553, 0.25263120532035827),      
RealParameter('Relatedness[Specialistic Technical and scientific activities,ICT information and services]', 0.020512799918651584, 0.030769199877977375),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Aerospace construction and engineering]', 0.0380952000617981, 0.05714280009269714),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Specialistic Technical and scientific activities]', 0.0, 0.0),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Manufacturing of measurement instruments of navigation and watchmaking]', 0.033333361148834235, 0.05000004172325135),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Editing audiovisual and diffusion]', 0.0, 0.0),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Manufacturing of communication equipment]', 0.0, 0.0),
RealParameter('Relatedness[Specialistic Technical and scientific activities,Production and distribution of gas vapour and AC]', 0.15000000000000002, 0.22499999999999998),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Pharmaceutical Industry]', 0.06666663885116578, 0.09999995827674865),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Chemical industry]', 0.06666663885116578, 0.09999995827674865),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Automotive industry]', 0.029629600048065186, 0.044444400072097774),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,ICT information and services]', 0.03720928132534027, 0.055813921988010405),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Aerospace construction and engineering]', 0.0, 0.0),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Specialistic Technical and scientific activities]', 0.033333361148834235, 0.05000004172325135),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.0),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Editing audiovisual and diffusion]', 0.0, 0.0),  
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Manufacturing of communication equipment]', 0.11851840019226073, 0.17777760028839107),
RealParameter('Relatedness[Manufacturing of measurement instruments of navigation and watchmaking,Production and distribution of gas vapour and AC]', 0.034782639145851134, 0.052173958718776704),
RealParameter('Relatedness[Editing audiovisual and diffusion,Pharmaceutical Industry]', 0.0, 0.0),
RealParameter('Relatedness[Editing audiovisual and diffusion,Chemical industry]', 0.0, 0.0),
RealParameter('Relatedness[Editing audiovisual and diffusion,Automotive industry]', 0.0, 0.0),
RealParameter('Relatedness[Editing audiovisual and diffusion,ICT information and services]', 0.25806479454040526, 0.3870971918106079),
RealParameter('Relatedness[Editing audiovisual and diffusion,Aerospace construction and engineering]', 0.0, 0.0),
RealParameter('Relatedness[Editing audiovisual and diffusion,Specialistic Technical and scientific activities]', 0.0, 0.0),
RealParameter('Relatedness[Editing audiovisual and diffusion,Manufacturing of measurement instruments of navigation and watchmaking]', 0.0, 0.0),  
RealParameter('Relatedness[Editing audiovisual and diffusion,Editing audiovisual and diffusion]', 0.0, 0.0),
RealParameter('Relatedness[Editing audiovisual and diffusion,Manufacturing of communication equipment]', 0.03076919913291931, 0.04615379869937897),
RealParameter('Relatedness[Editing audiovisual and diffusion,Production and distribution of gas vapour and AC]', 0.0, 0.0),
RealParameter('Relatedness[Manufacturing of communication equipment,Pharmaceutical Industry]', 0.04210528135299683, 0.06315792202949523),
RealParameter('Relatedness[Manufacturing of communication equipment,Chemical industry]', 0.04210528135299683, 0.06315792202949523),
RealParameter('Relatedness[Manufacturing of communication equipment,Automotive industry]', 0.0, 0.0),
RealParameter('Relatedness[Manufacturing of communication equipment,ICT information and services]', 0.12000000476837161, 0.1800000071525574),      
RealParameter('Relatedness[Manufacturing of communication equipment,Aerospace construction and engineering]', 0.0, 0.0),
RealParameter('Relatedness[Manufacturing of communication equipment,Specialistic Technical and scientific activities]', 0.0, 0.0),
RealParameter('Relatedness[Manufacturing of communication equipment,Manufacturing of measurement instruments of navigation and watchmaking]', 0.11851840019226073, 0.17777760028839107),
RealParameter('Relatedness[Manufacturing of communication equipment,Editing audiovisual and diffusion]', 0.03076919913291931, 0.04615379869937897),
RealParameter('Relatedness[Manufacturing of communication equipment,Manufacturing of communication equipment]', 0.0, 0.0),
RealParameter('Relatedness[Manufacturing of communication equipment,Production and distribution of gas vapour and AC]', 0.033333361148834235, 0.05000004172325135),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Pharmaceutical Industry]', 0.0, 0.0),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Chemical industry]', 0.11034480333328248, 0.1655172049999237),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Automotive industry]', 0.0, 0.0),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,ICT information and services]', 0.0, 0.0),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Aerospace construction and engineering]', 0.0, 0.0),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Specialistic Technical and scientific activities]', 0.15000000000000002, 0.22499999999999998),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Manufacturing of measurement instruments of navigation and watchmaking]', 0.034782639145851134, 0.052173958718776704),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Editing audiovisual and diffusion]', 0.0, 0.0),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Manufacturing of communication equipment]', 0.033333361148834235, 0.05000004172325135),
RealParameter('Relatedness[Production and distribution of gas vapour and AC,Production and distribution of gas vapour and AC]', 0.0, 0.0)
]
    # list of all the TimeSeriesOutcome of interest
    sector_names = [
        'Pharmaceutical Industry',
        'Chemical industry',
        'Automotive industry',
        'ICT information and services',
        'Aerospace construction and engineering',
        'Specialistic Technical and scientific activities',
        'Manufacturing of measurement instruments of navigation and watchmaking',
        'Editing audiovisual and diffusion',
        'Manufacturing of communication equipment',
        'Production and distribution of gas vapour and AC'
    ]
    model.outcomes = [
        TimeSeriesOutcome(f'Industry knowledge size[{s}]') for s in sector_names
    ]
    
    sa_results = perform_experiments(model, scenarios=452, uncertainty_sampling=Samplers.SOBOL)
    save_results(sa_results, "./sobol sensitivy run Jacobs.tar.gz")

    experiments, outcomes = sa_results
    ema_logging.log_to_stderr(ema_logging.INFO)

    # build the SALib problem dict
    problem = get_SALib_problem(model.levers)

     # Container for sensitivity data
    sensitivity = {}

    for s in sector_names:
        ts = outcomes[f'Industry knowledge size[{s}]']  # shape (Nruns, T)
        Y = np.max(ts, axis=1)  # scalar summary: max over time
        Si = sobol.analyze(problem, Y, calc_second_order=True, print_to_console=False)
        sensitivity[s] = Si

    df = pd.DataFrame({
    s: sensitivity[s]['ST'] for s in sector_names}, index=problem['names']).T  # sectors×levers
    df['ST_max'] = df.max(axis=1)
    df = df.sort_values('ST_max', ascending=False)
    n_sectors = len(sector_names)
    n_cols = 2
    n_rows = (n_sectors + 1) // n_cols

    # Create DataFrame for ST and sort
    st_df = pd.DataFrame({s: sensitivity[s]['ST'] for s in sector_names}, index=problem['names']).T
    st_df['ST_max'] = st_df.max(axis=1)
    st_df = st_df.sort_values('ST_max', ascending=False)

    # Map levers to letters
    lever_numbers = {name: str(i+1) for i, name in enumerate(problem['names'])}

    for sector in df.index:
        # pull out all indices
        st_all     = sensitivity[sector]['ST']
        s1_all     = sensitivity[sector]['S1']
        st_conf_all= sensitivity[sector]['ST_conf']
        s1_conf_all= sensitivity[sector]['S1_conf']
        names_all  = problem['names']

        # sort by total‐order descending and pick top 25
        sorted_idx = np.argsort(st_all)[::-1][:25]
        top_names    = [names_all[i]       for i in sorted_idx]
        top_st       = st_all[sorted_idx]
        top_s1       = s1_all[sorted_idx]
        top_st_conf  = st_conf_all[sorted_idx]
        top_s1_conf  = s1_conf_all[sorted_idx]

        # create x positions and labels
        x_pos       = np.arange(len(top_names))
        x_labels    = [lever_numbers[n] for n in top_names]

        # plot
        fig, ax = plt.subplots(figsize=(8,4))
        ax.bar(x_pos,       top_st,    yerr=top_st_conf, alpha=0.7, label='Total-order')
        ax.bar(x_pos,       top_s1,    yerr=top_s1_conf, alpha=0.7, label='First-order')

        # tick with lever numbers
        ax.set_xticks(x_pos)
        ax.set_xticklabels(x_labels, rotation=0, fontsize=11)

        ax.set_title(f"{sector}  (top 25 by ST)")
        ax.set_ylabel("Sobol index")
        ax.legend()  

        # legend mapping numbers → full names
        handles, labels = [], []
        for name in top_names:
            num = lever_numbers[name]
            handles.append(Line2D([], [], linestyle='none'))
            labels.append(f"{num}: {name}")
        ax.legend(handles, labels,
                bbox_to_anchor=(1.05, 1),
                loc='upper left',
                fontsize='small')


        plt.tight_layout()
        plt.show()
        

# Create the ST matrix and rename columns to lever letters
    st_matrix = df.loc[:, problem['names']].rename(columns=lever_numbers)
    # Plot heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(st_matrix,
                cmap='viridis',
                annot=False,
                ax=ax,
                cbar_kws={'label': 'ST index'})

    # Axis labels
    ax.set_title("Total-order Sobol indices (sectors × levers)")
    ax.set_xlabel("Levers (letter-coded)")
    ax.set_ylabel("Sectors (sorted by max ST)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

    plt.tight_layout()
    plt.show()

    # Add a custom legend on the right, showing what each letter means
    handles = [plt.Line2D([], [], linestyle='none') for _ in lever_numbers]
    labels = [f"{letter}: {name}" for name, letter in lever_numbers.items()]
    fig.legend(handles, labels,
        loc='center left',
        bbox_to_anchor=(1.05, 0.5),
        title="Levers",
        fontsize='small')

# Create a table with rows = (sector, lever), columns = S1, ST, S1_conf, ST_conf
sobol_table = []

for sector in sector_names:
    Si = sensitivity[sector]  # your precomputed sensitivity results
    for i, lever in enumerate(problem['names']):
        sobol_table.append({
            'Sector': sector,
            'Lever': lever,
            'S1': Si['S1'][i],
            'S1_conf': Si['S1_conf'][i],
            'ST': Si['ST'][i],
            'ST_conf': Si['ST_conf'][i]
        })

# Convert to DataFrame
sobol_df = pd.DataFrame(sobol_table)

# Sort for better readability
sobol_df = sobol_df.sort_values(['Sector', 'ST'], ascending=[True, False])
sobol_df['Lever_no'] = sobol_df['Lever'].map(lever_numbers)

# Save to Excel (or change to .csv if needed)
sobol_df.to_excel('C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/sobol_results_by_sector Jacobs.xlsx', index=False)

# Optional: display preview
print(sobol_df.head())