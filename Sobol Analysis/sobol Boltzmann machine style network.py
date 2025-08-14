import numpy as np
import pandas as pd
from ema_workbench.em_framework.salib_samplers import get_SALib_problem
from ema_workbench import (Samplers, TimeSeriesOutcome, perform_experiments, RealParameter, ema_logging, MultiprocessingEvaluator, save_results)
from SALib.analyze import sobol
from ema_workbench.connectors.vensim import VensimModel
from ema_workbench import load_results
import networkx as nx
import matplotlib.pyplot as plt


experiments, outcomes = load_results("C:/Users/Allis/sobol sensitivy run Jacobs no relatedness.tar.gz")

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
RealParameter('Relative share women in fertile age', 0.4, 0.6)
]

    model.outcomes = [
            TimeSeriesOutcome(f'Industry knowledge size[{s}]') for s in sector_names
        ]

problem = get_SALib_problem(model.levers)  # make sure you define your model.levers

sensitivity = {}
for sector in sector_names:
    ts = outcomes[f'Industry knowledge size[{sector}]']
    Y = np.max(ts, axis=1)
    Si = sobol.analyze(problem, Y, calc_second_order=True, print_to_console=False)
    sensitivity[sector] = Si

lever_names = problem['names']
all_ST = np.stack([sensitivity[s]['ST'] for s in sector_names])
all_S1 = np.stack([sensitivity[s]['S1'] for s in sector_names])
all_S2 = np.stack([sensitivity[s]['S2'] for s in sector_names])

# Function to generate octagon layout
def octagon_layout(nodes, radius=1.0):
    layout = {}
    n = len(nodes)
    for i, node in enumerate(nodes):
        angle = 2 * np.pi * i / n
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        layout[node] = (x, y)
    return layout

# Function to plot network graph for a sector with octagon layout
def plot_sector_network(sector):
    st_all = sensitivity[sector]['ST']
    s1_all = sensitivity[sector]['S1']
    s2_all = sensitivity[sector]['S2']
    names_all = problem['names']

    # Select top 8 levers by ST
    sorted_idx = np.argsort(st_all)[::-1][:8]
    top_names = [names_all[i] for i in sorted_idx]
    top_st = st_all[sorted_idx]
    top_s1 = s1_all[sorted_idx]
    top_s2 = s2_all[np.ix_(sorted_idx, sorted_idx)]

    # Normalize ST, S1, and S2 for visualization
    st_norm = (top_st - np.min(top_st)) / (np.max(top_st) - np.min(top_st)) + 0.1
    s1_norm = (top_s1 - np.min(top_s1)) / (np.max(top_s1) - np.min(top_s1)) + 0.1
    s2_norm = top_s2 / np.max(top_s2) if np.max(top_s2) > 0 else top_s2

    # Create graph
    G = nx.Graph()
    for i, name in enumerate(top_names):
        G.add_node(name, size=st_norm[i], s1=s1_norm[i])
    for i in range(len(top_names)):
        for j in range(i + 1, len(top_names)):
            weight = s2_norm[i, j]
            if weight > 0:
                G.add_edge(top_names[i], top_names[j], weight=weight)

    # Use octagon layout
    pos = octagon_layout(top_names)

    # Plotting
    plt.figure(figsize=(8, 8))
    edge_widths = [G[u][v]['weight'] * 5 for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6, edge_color='gray')

    node_sizes = [G.nodes[n]['size'] * 2000 for n in G.nodes()]
    node_colors = [G.nodes[n]['s1'] for n in G.nodes()]
    nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes,
                                   node_color=node_colors, cmap='Reds', alpha=0.8)

    # Labels as lever numbers
    mapping = {name: str(sorted_idx[i] + 1) for i, name in enumerate(top_names)}
    print(mapping)
    nx.draw_networkx_labels(G, pos, labels=mapping, font_size=10)

    plt.colorbar(nodes, label='Normalized S1')
    plt.title(f"{sector}\nNode size ∝ ST, Color ∝ S1, Edge width ∝ S2")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# 7. Generate one network per sector
for sector in sector_names:
    plot_sector_network(sector)
