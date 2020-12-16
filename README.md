# FEP and Active Inference Paper Repository 
This repository provides a list of papers that I believe are interesting and influential on the Free-Energy-Principle, or in Active Inference. If you believe I have missed any papers, please contact me at *beren@millidge.name* or make a pull request with the information about the paper. I will be happy to include it. 

## FEP Outline 
This list is of papers focused specifically on the abstract mathematical formulation of the Free-Energy-Principle (FEP). The FEP is a theory which tries to determine the behaviours a non-equilibrium thermodynamical system *must* exhibit if it is to maintain itself as a separate entity over time. It argues that any such system must minimize a quantity called the free energy and that, over the course of this minimisation, behaviour much like action and perception must emerge. 
 
The key prerequisites for the FEP is that a 'system' has a special kind of statistical separation from the world called a Markov Blanket, which it must maintain if it is to remain a system, and that the system possesses a non-equilibrium steady state which it self-organises to and tries to maintain over time against the dissipative forces of entropy. 
 
Much of the work in the FEP has been applying its general tenets to understand biological far-from-equilibrium systems, especially the brain. 
 
If you are just starting out, I reccomend reading all the papers in the 'Survey' section in order. These are all great tutorials or overviews which should give you a great grounding in the intuitions of the theory, and then the later two tutorials should start building up much of the mathematical core of the theory (especially around predictive coding). 
 
- [Surveys](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#surveys)
- [Classics](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#classics)
- [Philosophical Analyses](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#philosophical-analyses)
- [Self-Organisation and Markov Blankets](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#self-organisation-and-markov-blankets)
- [Information Geometry](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#information-geometry)

## Surveys
- [**What does the free energy principle tell us about the brain?**](https://arxiv.org/abs/1901.07945) , (2019) by  Samuel J Gershman  [[bib]](bibtex.bib#L1-L8) 
 
 *This provides a great high level introduction to the basic ideas and intuitions of the FEP, with a small amount of crucial mathematical background.* 
- [**The free-energy principle: a unified brain theory?**](https://www.uab.edu/medicine/cinl/images/KFriston_FreeEnergy_BrainTheory.pdf) , (2010) by  Karl Friston  [[bib]](bibtex.bib#L11-L22) 
 
 *This provides a great overview for the initial intuitions behind the FEP and its application to the brain.* 
- [**A tutorial on the free-energy framework for modelling perception and learning**](https://www.sciencedirect.com/science/article/pii/S0022249615000759) , (2017) by  Rafal Bogacz  [[bib]](bibtex.bib#L27-L37) 
 
 *This is a great review which introduces the basics of predictive coding and the FEP, including the maths and contains MATLAB sample code. If you want to start seriously diving into the maths, I would start here.* 
- [**The free energy principle for action and perception: A mathematical review**](https://www.sciencedirect.com/science/article/pii/S0022249617300962) , (2017) by  Christopher L Buckley and  Chang Sub Kim and  Simon McGregor and  Anil K Seth  [[bib]](bibtex.bib#L41-L51) 
 
 *This is a fantastic review which presents a complete walkthrough of the mathematical basis of the Free Energy Principle and Variational Inference, and derives predictive coding and (continuous time and state) active inference. I would reccomend reading this after Bogacz' tutorial (although be prepared -- it is a long and serious read)* 

## Classics
- [**A free energy principle for a particular physics**](https://arxiv.org/pdf/1906.10184.pdf) , (2019) by  Karl Friston  [[bib]](bibtex.bib#L55-L62) 
 
 *This is Karl's magisterial monograph, and contains the most comprehensive description of the FEP to date* 
- [**A free energy principle for the brain**](https://www.sciencedirect.com/science/article/pii/S092842570600060X?casa_token=rPwSn8wQvEkAAAAA:5QeLri0QzrjAC8QYtNljoqjn0nZzRJIoBso67Uw3eY9VSFdUqcIm4mkqPBNZCwYQM8PM_VdkFfE) , (2006) by  Karl Friston and  James Kilner and  Lee Harrison  [[bib]](bibtex.bib#L66-L77) 
 
 *Perhaps the earliest paper describing the FEP. Provides a great description of the fundamental intuitions behind the theory (in needs of living systems to reduce their internal entropy to keep conditions within homeostatic bounds)* 
- [**A theory of cortical responses**](https://royalsocietypublishing.org/doi/abs/10.1098/rstb.2005.1622?casa_token=9zU-Epc4Iw4AAAAA%3AmYQq9buUvH2tb1xtL8VXFp0oHtJVGZ_4MSymueoSBUreJAhsqEOB3D-fXJnSqMnbTYP3VBo0BxwHWYE) , (2005) by  Karl Friston  [[bib]](bibtex.bib#L80-L91) 
 
 *An early but complete description of predictive coding as an application of the FEP and variational inference under Gaussian and Laplace assumptions. Also surprisingly readable. This is core reading on predictive coding and the FEP* 
- [**Learning and inference in the brain**](https://www.sciencedirect.com/science/article/pii/S0893608003002454?casa_token=Z-HR_To6rxwAAAAA:88ducipot59VHoRHJu1Ej6Kz5oLn-RMooUV9rR1fnkH50D5aNvLNENIF2XBa_3tZ0izMX5U2ED8) , (2003) by  Karl Friston  [[bib]](bibtex.bib#L93-L104) 
- [**Reinforcement learning or active inference?**](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0006421) , (2009) by  Karl J Friston and  Jean Daunizeau and  Stefan J Kiebel  [[bib]](bibtex.bib#L105-L116) 
 
 *The earliest paper (I think) on active inference. Introduces the motivation behind the continuous state and time formulation of active inference. Shows how predictive coding can be used to learn actions as well as observations (by treating them the same)* 
- [**Action understanding and active inference**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3491875/) , (2011) by  Karl Friston and  J{\'e}r{\'e}mie Mattout and  James Kilner  [[bib]](bibtex.bib#L119-L130) 
 
 *Goes deep into the neuroscientific intuitions behind why you might want to think about action as a predicted observation and not a latent variable for biological brains. Presents Karl's view that action happens primarily at the periphery through simple 'reflex arcs' while all the real work is done by the generative models generating predictions.* 
- [**A free energy principle for biological systems**](https://www.mdpi.com/1099-4300/14/11/2100) , (2012) by  Friston Karl  [[bib]](bibtex.bib#L132-L143) 
- [**Of woodlice and men**](https://www.aliusresearch.org/uploads/9/1/6/0/91600416/alius_bulletin_n%C2%B02__2018_.pdf#page=27) , (2018) by  Martin Fortier and  Daniel A Friedman  [[bib]](bibtex.bib#L144-L152) 
 
 *A great interview with Karl. Goes into a lot of his personal motivations underlying his work on the FEP. I would recommend this perhaps as an initial place to start out if you know nothing of the FEP to grasp the underlying motivations of *what* it is trying to explain.* 
- [**The history of the future of the Bayesian brain**](https://www.sciencedirect.com/science/article/pii/S1053811911011657) , (2012) by  Karl Friston  [[bib]](bibtex.bib#L154-L165) 
- [**Free energy, value, and attractors**](https://www.hindawi.com/journals/cmmm/2012/937860/) , (2012) by  Karl Friston and  Ping Ao  [[bib]](bibtex.bib#L166-L175) 
 
 *Mathematical paper by Karl and Ping Ao which begins fleshing out formally the notion of desires as attractors* 
- [**Attention, uncertainty, and free-energy**](https://www.frontiersin.org/articles/10.3389/fnhum.2010.00215/full) , (2010) by  Harriet Feldman and  Karl Friston  [[bib]](bibtex.bib#L177-L187) 
 
 *Makes a conjectured link between precision in predictive coding and attention in the brain.* 
- [**Hierarchical models in the brain**](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000211) , (2008) by  Karl Friston  [[bib]](bibtex.bib#L189-L200) 
 
 *Presents the 'full-construct' predictive coding model with both hierarchies and generalised coordinates.* 
- [**DEM: a variational treatment of dynamic systems**](https://www.sciencedirect.com/science/article/pii/S1053811908001894?casa_token=RBtljR9mpKMAAAAA:EAAQB59MLINQl8q4it_Pxnz6EbRaqvO0mMey40hdf29Qy0kKkH69qWN24jnmhcOXamuXWBqFAG4) , (2008) by  Karl J Friston and  N Trujillo-Barreto and  Jean Daunizeau  [[bib]](bibtex.bib#L202-L213) 
 
 *Extends predictive coding to generalised coordinates, and derives the necessary inference algorithms for working with them -- i.e. DEM, dynamic expectation maximisation.* 
- [**Generalised filtering**](https://www.hindawi.com/journals/mpe/2010/621670/) , (2010) by  Karl Friston and  Klaas Stephan and  Baojuan Li and  Jean Daunizeau  [[bib]](bibtex.bib#L215-L224) 
- [**Surfing uncertainty: Prediction, action, and the embodied mind**](https://books.google.co.uk/books?hl=en&lr=&id=TnqECgAAQBAJ&oi=fnd&pg=PP1&dq=andy+clark+surfing+uncertainty&ots=aurm4jE3NO&sig=KxeHGJ6YJJdN9tKyr6snwDyBBKg&redir_esc=y#v=onepage&q=andy%20clark%20surfing%20uncertainty&f=false) , (2015) by  Andy Clark  [[bib]](bibtex.bib#L322-L329) 
- [**Variational filtering**](https://www.sciencedirect.com/science/article/pii/S1053811908002462?casa_token=bzK7h_aIzY0AAAAA:rg1CzE6vNo-cktIHO_9EAoqmR5Zpy89klEn-Wy3NAzMoR8NcWgaF5_zEzyhrRB76N5RPyCZTIlY) , (2008) by  Karl J Friston  [[bib]](bibtex.bib#L855-L866) 
 
 *Foundational treatment of variational inference for dynamical systems, as represented in generalised coordinates. Also relates variational filtering to other non-variational schemes like particle filtering and Kalman filtering.* 
- [**Action and behavior: a free-energy formulation**](https://link.springer.com/article/10.1007/s00422-010-0364-z) , (2010) by  Karl J Friston and  Jean Daunizeau and  James Kilner and  Stefan J Kiebel  [[bib]](bibtex.bib#L939-L950) 

## Philosophical Analyses
- [**A tale of two densities: Active inference is enactive inference**](https://journals.sagepub.com/doi/pdf/10.1177/1059712319862774) , (2020) by  Maxwell JD Ramstead and  Michael D Kirchhoff and  Karl J Friston  [[bib]](bibtex.bib#L225-L236) 
- [**Answering Schr{\"o}dinger's question: A free-energy formulation**](https://www.sciencedirect.com/science/article/pii/S1571064517301409) , (2018) by  Maxwell James D{\'e}sormeau Ramstead and  Paul Benjamin Badcock and  Karl John Friston  [[bib]](bibtex.bib#L237-L247) 
- [**Thinking through other minds: A variational approach to cognition and culture**](https://royalsocietypublishing.org/doi/full/10.1098/rsif.2017.0685) , (2020) by  Samuel PL Veissi{\`e}re and  Axel Constant and  Maxwell JD Ramstead and  Karl J Friston and  Laurence J Kirmayer  [[bib]](bibtex.bib#L248-L257) 
- [**TTOM in action: Refining the variational approach to cognition and culture**](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/ttom-in-action-refining-the-variational-approach-to-cognition-and-culture/ADD060A9EE6937A3104FA23290F2C519) , (2020) by  Samuel PL Veissi{\`e}re and  Axel Constant and  Maxwell JD Ramstead and  Karl J Friston and  Laurence J Kirmayer  [[bib]](bibtex.bib#L258-L267) 
- [**What does the free energy principle tell us about the brain?**](https://arxiv.org/abs/1901.07945) , (2019) by  Samuel J Gershman  [[bib]](bibtex.bib#L1-L8) 
 
 *This provides a great high level introduction to the basic ideas and intuitions of the FEP, with a small amount of crucial mathematical background.* 
- [**The anticipating brain is not a scientist: the free-energy principle from an ecological-enactive perspective**](https://link.springer.com/article/10.1007/s11229-016-1239-1) , (2018) by  Jelle Bruineberg and  Julian Kiverstein and  Erik Rietveld  [[bib]](bibtex.bib#L276-L287) 
- [**Predictive processing and the representation wars**](https://link.springer.com/article/10.1007/s11023-017-9441-6) , (2018) by  Daniel Williams  [[bib]](bibtex.bib#L288-L299) 
- [**Whatever next? Predictive brains, situated agents, and the future of cognitive science**](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-science/33542C736E17E3D1D44E8D03BE5F4CD9) , (2013) by  Andy Clark  [[bib]](bibtex.bib#L300-L311) 
- [**Predictions in the eye of the beholder: an active inference account of Watt governors**](https://www.mitpressjournals.org/doi/abs/10.1162/isal_a_00288) , (2020) by  Manuel Baltieri and  Christopher L Buckley and  Jelle Bruineberg  [[bib]](bibtex.bib#L312-L321) 
- [**From allostatic agents to counterfactual cognisers: active inference, biological regulation, and the origins of cognition**](https://link.springer.com/article/10.1007/s10539-020-09746-2) , (2020) by  Andrew W Corcoran and  Giovanni Pezzulo and  Jakob Hohwy  [[bib]](bibtex.bib#L796-L807) 
- [**Interoceptive inference, emotion, and the embodied self**](https://www.sciencedirect.com/science/article/pii/S1364661313002118) , (2013) by  Anil K Seth  [[bib]](bibtex.bib#L808-L819) 
- [**Active interoceptive inference and the emotional brain**](https://royalsocietypublishing.org/doi/full/10.1098/rstb.2016.0007) , (2016) by  Anil K Seth and  Karl J Friston  [[bib]](bibtex.bib#L820-L831) 
- [**The cybernetic Bayesian brain**](https://open-mind.net/papers/the-cybernetic-bayesian-brain) , (2014) by  Anil K Seth  [[bib]](bibtex.bib#L832-L839) 
- [**Presence, objecthood, and the phenomenology of predictive perception**](https://www.tandfonline.com/doi/full/10.1080/17588928.2015.1026888?casa_token=IA7GL_oM2VAAAAAA%3AXkJ7HbhxHcW7qCdSWyRSerOo8iZevM3x_8QV1b7C7qAvAqJMveeq4IeGRBTCCbQOCJ6Ix9p70VkKww) , (2015) by  Anil K Seth  [[bib]](bibtex.bib#L840-L851) 
- [**The Math is not the Territory: Navigating the Free Energy Principle**](http://philsci-archive.pitt.edu/18315/) , (2020) by  Mel Andrews  [[bib]](bibtex.bib#L911-L917) 

## Self-Organisation and Markov Blankets
- [**Life as we know it**](https://royalsocietypublishing.org/doi/full/10.1098/rsif.2013.0475) , (2013) by  Karl Friston  [[bib]](bibtex.bib#L330-L341) 
- [**Knowing one's place: a free-energy approach to pattern regulation**](https://royalsocietypublishing.org/doi/full/10.1098/rsif.2014.1383) , (2015) by  Karl Friston and  Michael Levin and  Biswa Sengupta and  Giovanni Pezzulo  [[bib]](bibtex.bib#L342-L353) 
- [**Morphogenesis as Bayesian inference: A variational approach to pattern formation and control in complex biological systems**](https://www.sciencedirect.com/science/article/pii/S1571064519300909?casa_token=IrMsxOkLhfYAAAAA:2agLQQPi8aeYTxxqotIPCyEzsHbpvOLwf_0eK5oW2Li0Gi5THHn2XRpWYfNT99M0Xy5pPD_S9CA) , (2019) by  Franz Kuchling and  Karl Friston and  Georgi Georgiev and  Michael Levin  [[bib]](bibtex.bib#L354-L362) 
- [**Neural and phenotypic representation under the free-energy principle**](https://www.sciencedirect.com/science/article/pii/S0149763420306643?casa_token=16rC0ManFBUAAAAA:3mbntn5I7fObnA_Y397rvZbWrnUzkqmALD1LtS88tGrIRxbw9RQvU55XJuH-zKdBi6tPaN9faDM) , (2020) by  Maxwell JD Ramstead and  Casper Hesp and  Alexander Tschantz and  Ryan Smith and  Axel Constant and  Karl Friston  [[bib]](bibtex.bib#L363-L371) 
- [**Parcels and particles: Markov blankets in the brain**](https://arxiv.org/abs/2007.09704) , (2020) by  Karl J Friston and  Erik D Fagerholm and  Tahereh S Zarghami and  Thomas Parr and  In{\^e}s Hip{\'o}lito and  Lo{\"\i}c Magrou and  Adeel Razi  [[bib]](bibtex.bib#L372-L379) 
- [**Markov blankets in the brain**](https://arxiv.org/abs/2006.02741) , (2020) by  Ines Hipolito and  Maxwell Ramstead and  Laura Convertino and  Anjali Bhat and  Karl Friston and  Thomas Parr  [[bib]](bibtex.bib#L380-L387) 
- [**Modules or Mean-Fields?**](https://www.mdpi.com/1099-4300/22/5/552) , (2020) by  Thomas Parr and  Noor Sajid and  Karl J Friston  [[bib]](bibtex.bib#L388-L399) 
- [**Biological self-organisation and Markov blankets**](https://www.biorxiv.org/content/10.1101/227181v1.abstract) , (2017) by  Ensor Rafael Palacios and  Adeel Razi and  Thomas Parr and  Michael Kirchhoff and  Karl Friston  [[bib]](bibtex.bib#L400-L409) 
- [**The Emperor’s New Markov Blankets**](http://philsci-archive.pitt.edu/18467/) , (2020) by  Jelle Bruineberg and  Krzysztof Dolega and  Joe Dewhurst and  Manuel Baltieri  [[bib]](bibtex.bib#L564-L570) 

## Information Geometry
- [**Markov blankets, information geometry and stochastic thermodynamics**](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2019.0159) , (2020) by  Thomas Parr and  Lancelot Da Costa and  Karl Friston  [[bib]](bibtex.bib#L410-L421) 
 
 
## Active Inference Outline 
Active Inference is a process theory of neurobiological function inspired by and closely related to the FEP. However Active Inference stands independent of the FEP and can be true even if the FEP is not, and similarly can potentially be falsified without impacting the FEP. The core idea behind Active Inference is the idea that the brain performs both action and perception by variational inference on a unified objective function. 
 
In effect, the key idea behind active inference is that our brains possess powerful probabilistic generative models and inference engines, and that to select actions, we repurpose this powerful capacity we use for perception to also *infer* potential actions. Hence *Active* Inference. 
 
This high-level description leaves open the exact *type* of models and inference being used for action inference in the brain. The active inference literature contains three clear strands of work, which correspond to different assumptions on the exact form of generative models which are proposed to be utilized by the brain. *Discrete* active inference focuses on models of discrete state-spaces parametrised by categorical distributions and transition matrices. *Continuous* active inference focuses on the continuous time case with (generally) linear dynamics, and *Deep* active inference focuses on using deep neural networks to 'scale up' active inference by amortising probabilistic distributions with learned maps. 
The discrete-state-space work has close similarities with bandit-problems and neuroscience tasks and forms a tractable test-bed to understand different kinds of behaviour. Most of the work of creating active inference models of brain function (or dysfunction) lies within this paradigm. Continuous active inference, which is being used for robot control, has close links to classical control theory, while Deep active inference has close links with reinforcement learning and machine learning. 
 
The task of inferring actions (requiring detailed models of future outcomes given these actions), is a subtly more complex task than simply inferring the immediate causes of sensory data as in perceptual inference. It therefore requires different objective functionals (the *expected* free energy) and potentially more advanced message-passing inference algorithms. This work is summarised in the 'Message Passing and Free Energies' section. 
 

 
- [Surveys and Tutorials](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#surveys-and-tutorials)
- [Discrete State Space Formulation](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#discrete-state-space-formulation)
- [Continuous Time Formulation](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#continuous-time-formulation)
- [Message Passing and Free Energies](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#message-passing-and-free-energies)
- [Active Inference for Control Theory/Robotics](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#active-inference-for-control-theory/robotics)
- [Neuroscience and Computational Psychiatry Applications](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#neuroscience-and-computational-psychiatry-applications)
- [Deep Active Inference](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/README.md#deep-active-inference)

## Surveys and Tutorials
- [**Active inference on discrete state-spaces: a synthesis**](https://arxiv.org/abs/2001.07203) , (2020) by  Lancelot Da Costa and  Thomas Parr and  Noor Sajid and  Sebastijan Veselic and  Victorita Neacsu and  Karl Friston  [[bib]](bibtex.bib#L422-L429) 
 
 *This is a great and thorough tutorial on discrete-state-space active inference. I would reccomend it to everybody new to the field.* 

## Discrete State Space Formulation
- [**Active inference and epistemic value**](https://www.tandfonline.com/doi/full/10.1080/17588928.2015.1020053?casa_token=IiMRlTIPAXUAAAAA%3ASvxdCeRv4yruAnjsNhletPuaWzdb8dfm-5s1YvTBaup1IgHNChHDKgCe1DY40DAvYHK6ZO4_guujAA) , (2015) by  Karl Friston and  Francesco Rigoli and  Dimitri Ognibene and  Christoph Mathys and  Thomas Fitzgerald and  Giovanni Pezzulo  [[bib]](bibtex.bib#L431-L442) 
 
 *Introduces the main intuitions behind active inference, as well as the crucial epistemic foraging behaviour of the expected free energy. Illustrated on a simple T-maze task.* 
- [**Active inference and learning**](https://www.sciencedirect.com/science/article/pii/S0149763416301336) , (2016) by  Karl Friston and  Thomas FitzGerald and  Francesco Rigoli and  Philipp Schwartenbeck and  Giovanni Pezzulo and others  [[bib]](bibtex.bib#L444-L454) 
- [**Active inference and agency: optimal control without cost functions**](https://link.springer.com/article/10.1007/s00422-012-0512-8) , (2012) by  Karl Friston and  Spyridon Samothrakis and  Read Montague  [[bib]](bibtex.bib#L455-L466) 
 
 *The first (I think) discrete-state-space paper on active inference. Notable for using the standard variational free energy as objective function and not the expected free energy. Describes some of the intuitions behind active inference.* 
- [**Active inference: a process theory**](https://www.mitpressjournals.org/doi/full/10.1162/NECO_a_00912) , (2017) by  Karl Friston and  Thomas FitzGerald and  Francesco Rigoli and  Philipp Schwartenbeck and  Giovanni Pezzulo  [[bib]](bibtex.bib#L468-L479) 
 
 *Provides a very good and thorough description of discrete-state-space active inference and ties its updates closely to neural physiology. I would reccomend this after the Da Costa introduction.* 
- [**Uncertainty, epistemics and active inference**](https://royalsocietypublishing.org/doi/full/10.1098/rsif.2017.0376) , (2017) by  Thomas Parr and  Karl J Friston  [[bib]](bibtex.bib#L481-L492) 
- [**Deep temporal models and active inference**](https://www.sciencedirect.com/science/article/pii/S0149763416307096) , (2018) by  Karl J Friston and  Richard Rosch and  Thomas Parr and  Cathy Price and  Howard Bowman  [[bib]](bibtex.bib#L493-L503) 
- [**Sophisticated Inference**](https://arxiv.org/abs/2006.04120) , (2020) by  Karl Friston and  Lancelot Da Costa and  Danijar Hafner and  Casper Hesp and  Thomas Parr  [[bib]](bibtex.bib#L571-L578) 
 
 *Introduces the next stage of active inference. 'Sophisticated' active inference, where agents make decisions not just on their beliefs about the future, but on how their beliefs will change in the future. Allows the simulation of real epistemic value -- i.e. act so as to change your beliefs in the future.* 
- [**Active inference: demystified and compared**](https://ui.adsabs.harvard.edu/abs/2019arXiv190910863S/abstract) , (2019) by  Noor Sajid and  Philip J Ball and  Karl J Friston  [[bib]](bibtex.bib#L580-L588) 
- [**The relationship between dynamic programming and active inference: The discrete, finite-horizon case**](https://arxiv.org/abs/2009.08111) , (2020) by  Lancelot Da Costa and  Noor Sajid and  Thomas Parr and  Karl Friston and  Ryan Smith  [[bib]](bibtex.bib#L589-L596) 
 
 *Discusses the relationship between active inference and dynamic programming solutions to reinforcement learning problems (i.e. Q learning, value functions etc). Shows that they are largely equivalent except with different objectives (Expected Free Energy vs Expected Discounted Reward).* 

## Continuous Time Formulation
- [**Reinforcement learning or active inference?**](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0006421) , (2009) by  Karl J Friston and  Jean Daunizeau and  Stefan J Kiebel  [[bib]](bibtex.bib#L105-L116) 
 
 *The earliest paper (I think) on active inference. Introduces the motivation behind the continuous state and time formulation of active inference. Shows how predictive coding can be used to learn actions as well as observations (by treating them the same)* 
- [**An active inference implementation of phototaxis**](https://www.mitpressjournals.org/doi/abs/10.1162/isal_a_011) , (2017) by  Manuel Baltieri and  Christopher L Buckley  [[bib]](bibtex.bib#L675-L684) 
 
 *Active inference in plants!!!* 
- [**PID control as a process of active inference with linear generative models**](https://www.mdpi.com/1099-4300/21/3/257) , (2019) by  Manuel Baltieri and  Christopher L Buckley  [[bib]](bibtex.bib#L687-L698) 
 
 *Active inference under a linear gaussian generative model can replicate PID, but also provide a natural method for learning the tuning coefficients (by understanding them as precisions).* 
- [**On Kalman-Bucy filters, linear quadratic control and active inference**](https://arxiv.org/abs/2005.06269) , (2020) by  Manuel Baltieri and  Christopher L Buckley  [[bib]](bibtex.bib#L700-L707) 
 
 *A key step towards understanding how active inference relates to classical control theory methods such as Kalman Filters and LQR control.* 
- [**Application of the Free Energy Principle to Estimation and Control**](https://arxiv.org/abs/1910.09823) , (2019) by  Thijs van de Laar and  Ay{\c{c}}a {\"O}z{\c{c}}elikkale and  Henk Wymeersch  [[bib]](bibtex.bib#L717-L724) 
 
 *Another approach to understanding how active inference relates to and extends classical control theory methods.* 
- [**The State Space Formulation of Active Inference: Towards Brain-Inspired Robot Control**](https://repository.tudelft.nl/islandora/object/uuid:0f56c37c-d22b-478b-8a85-dca615a8f419) , (2019) by  Sherin Grimbergen  [[bib]](bibtex.bib#L726-L732) 
 
 *An excellent overview and fantastic piece of work on the linear time-indepenent formulation of active inference and its relation to classical control theory.* 
- [**Hierarchical active inference: A theory of motivated control**](https://www.sciencedirect.com/science/article/pii/S1364661318300226) , (2018) by  Giovanni Pezzulo and  Francesco Rigoli and  Karl J Friston  [[bib]](bibtex.bib#L784-L795) 

## Message Passing and Free Energies
- [**The graphical brain: belief propagation and active inference**](https://www.mitpressjournals.org/doi/full/10.1162/NETN_a_00018) , (2017) by  Karl J Friston and  Thomas Parr and  Bert de Vries  [[bib]](bibtex.bib#L504-L515) 
 
 *Introduces the general factor-graph message passing viewpoint on active inference. Also introduces hierarchical active inference models.* 
- [**Neuronal message passing using Mean-field, Bethe, and Marginal approximations**](https://www.nature.com/articles/s41598-018-38246-3) , (2019) by  Thomas Parr and  Dimitrije Markovic and  Stefan J Kiebel and  Karl J Friston  [[bib]](bibtex.bib#L517-L528) 
 
 *Discusses in depth the different potential message passing inference algorithms which can be used to implement active inference on factor graphs.* 
- [**Active inference, belief propagation, and the bethe approximation**](https://www.mitpressjournals.org/doi/abs/10.1162/neco_a_01108) , (2018) by  Sarah Schw{\"o}bel and  Stefan Kiebel and  Dimitrije Markovi{\'c}  [[bib]](bibtex.bib#L530-L541) 
 
 *Introduces the Bethe free energy, as a result of making the Bethe approximation instead of the mean-field variational assumption to derive the message passing algorithms.* 
- [**Generalised free energy and active inference**](https://link.springer.com/article/10.1007/s00422-019-00805-w) , (2019) by  Thomas Parr and  Karl J Friston  [[bib]](bibtex.bib#L543-L554) 
- [**Whence the Expected Free Energy?**](https://arxiv.org/abs/2004.08128) , (2020) by  Beren Millidge and  Alexander Tschantz and  Christopher L Buckley  [[bib]](bibtex.bib#L555-L562) 
 
 *Discusses whether we can derive the expected free energy objective function on principled ground from the FEP, and discusses different potential objective functions for active inference.* 
- [**On the Relationship Between Active Inference and Control as Inference**](https://arxiv.org/abs/2006.12964) , (2020) by  Beren Millidge and  Alexander Tschantz and  Anil K Seth and  Christopher L Buckley  [[bib]](bibtex.bib#L610-L617) 
 
 *Discusses the relationship between Active Inference and Control as Inference, a variational framework for understanding action selection which has emerged from RL.* 

## Active Inference for Control Theory/Robotics
- [**Active inference and robot control: a case study**](https://royalsocietypublishing.org/doi/full/10.1098/rsif.2016.0616) , (2016) by  L{\'e}o Pio-Lopez and  Ange Nizard and  Karl Friston and  Giovanni Pezzulo  [[bib]](bibtex.bib#L734-L745) 
- [**Active inference body perception and action for humanoid robots**](https://arxiv.org/abs/1906.03022) , (2019) by  Guillermo Oliver and  Pablo Lanillos and  Gordon Cheng  [[bib]](bibtex.bib#L746-L753) 
- [**End-to-end pixel-based deep active inference for body perception and action**](https://arxiv.org/abs/2001.05847) , (2019) by  Cansu Sancaktar and  Pablo Lanillos  [[bib]](bibtex.bib#L754-L761) 
- [**Active inference for robot control: A factor graph approach**](https://pdfs.semanticscholar.org/e177/b21b0a7f43ad3969ceb42bd8f1d912ea8d43.pdf) , (2019) by  Mees Vanderbroeck and  Mohamed Baioumy and  Daan van der Lans and  Rens de Rooij and  Tiis van der Werf  [[bib]](bibtex.bib#L762-L771) 
- [**A novel adaptive controller for robot manipulators based on active inference**](https://ieeexplore.ieee.org/abstract/document/9000729/?casa_token=OBL93SqhogUAAAAA:6w99NtC-Fk7P0tIiXx6QmTNsWnPS-GKK0OtsJEz-HWgniXwpY0Rtue_qlc5Fe9HQ2vj0ropx7hM) , (2020) by  Corrado Pezzato and  Riccardo Ferrari and  Carlos Hern{\'a}ndez Corbato  [[bib]](bibtex.bib#L772-L783) 
- [**Adaptive robot body learning and estimation through predictive coding**](https://ieeexplore.ieee.org/document/8593684/) , (2018) by  Pablo Lanillos and  Gordon Cheng  [[bib]](bibtex.bib#L929-L938) 

## Neuroscience and Computational Psychiatry Applications
- [**Recent advances in the application of predictive coding and active inference models within clinical neuroscience**](https://onlinelibrary.wiley.com/doi/abs/10.1111/pcn.13138) , (2020) by  Ryan Smith and  Paul Badcock and  Karl J Friston  [[bib]](bibtex.bib#L868-L876) 
 
 *A comprehensive review of neuroscientific and computational psychiatry applications of the FEP and Active Inference.* 
- [**The Predictive Global Neuronal Workspace: A Formal Active Inference Model of Visual Consciousness**](https://www.sciencedirect.com/science/article/pii/S0301008220301738) , (2020) by  Christopher J Whyte and  Ryan Smith  [[bib]](bibtex.bib#L879-L887) 
- [**Neurocomputational mechanisms underlying emotional awareness: insights afforded by deep active inference and their potential clinical relevance**](https://www.sciencedirect.com/science/article/pii/S014976341930541X?casa_token=c1UILIbIsKYAAAAA:tQbclbvyieFsSPf_oqulTP8Manv6fU6CeI1iHGZe5Iq4TryLR4pGRjK0Y7RD4gZCfjJo02uWyvw) , (2019) by  Ryan Smith and  Richard D Lane and  Thomas Parr and  Karl J Friston  [[bib]](bibtex.bib#L888-L898) 
- [**Simulating emotions: An active inference model of emotional state inference and emotion concept learning**](https://www.frontiersin.org/articles/10.3389/fpsyg.2019.02844/full) , (2019) by  Ryan Smith and  Thomas Parr and  Karl J Friston  [[bib]](bibtex.bib#L900-L910) 
- [**The hierarchical basis of neurovisceral integration**](https://www.sciencedirect.com/science/article/pii/S014976341630673X?casa_token=V0kmqFxZWg4AAAAA:QE5VJB7jp6k22u8L7S7iWYh2_EiLV9a4gyXGUfSMIXOte_zYxGsH2YXUkvKY6PeDKriYy8nu11o) , (2017) by  Ryan Smith and  Julian F Thayer and  Sahib S Khalsa and  Richard D Lane  [[bib]](bibtex.bib#L918-L928) 
- [**Active inference in OpenAI gym: a paradigm for computational investigations into psychiatric illness**](https://www.sciencedirect.com/science/article/pii/S2451902218301617?casa_token=HRn2UHzCR18AAAAA:lTqZvwAL3WoYmchm2W2WYXKsastkTOVcEDpu9Fxtm5aZIfr6jmhexYHurChmmpFaNufNEpFuuPo) , (2018) by  Maell Cullen and  Ben Davey and  Karl J Friston and  Rosalyn J Moran  [[bib]](bibtex.bib#L951-L962) 

## Deep Active Inference
- [**Reinforcement Learning through Active Inference**](https://arxiv.org/abs/2002.12636) , (2020) by  Alexander Tschantz and  Beren Millidge and  Anil K Seth and  Christopher L Buckley  [[bib]](bibtex.bib#L620-L627) 
 
 *Demonstrates that the exploration afforded by the Expected Free Energy Objective is useful in a deep reinforcement learning setting. Also maintains uncertainty through model ensembles applied in a model-based RL setting.* 
- [**Scaling active inference**](https://ieeexplore.ieee.org/abstract/document/9207382/?casa_token=TfYG9cq3UvwAAAAA:Fn2oE7PCTGHlEN0jPQQE4P-qBiO_V-7xRFXXqYn7ubVoZeoiBd6ViBAxWf1L7j-R1wiKEOKvaXQ) , (2020) by  Alexander Tschantz and  Manuel Baltieri and  Anil K Seth and  Christopher L Buckley  [[bib]](bibtex.bib#L630-L639) 
 
 *Implements Deep Active Inference in a model-based RL setting using explicit planning with a transition model.* 
- [**Deep active inference as variational policy gradients**](https://www.sciencedirect.com/science/article/pii/S0022249620300298?casa_token=GQLxvJzk3zMAAAAA:uotM5EqPWP9SIUV-5N8vvNnkVWSqFlS8W03MZ_W9GYCoyhWGRAhN9YmGjiTIaxCGHd4iwrjzElg) , (2020) by  Beren Millidge  [[bib]](bibtex.bib#L641-L651) 
 
 *Implements deep active inference in a model-free policy gradient setting by amortising the learning of the expected-free-energy value function. Uses a transition model for the state-information gain term in the expected free energy.* 
- [**Deep active inference**](https://link.springer.com/article/10.1007/s00422-018-0785-7) , (2018) by  Kai Ueltzh{\"o}ffer  [[bib]](bibtex.bib#L653-L664) 
 
 *The first paper to try combining active inference with deep neural networks. Demonstrates the importance of the exploratory terms of the EFE to solve the mountain-car problem.* 
- [**Deep active inference agents using Monte-Carlo methods**](https://arxiv.org/abs/2006.04176) , (2020) by  Zafeirios Fountas and  Noor Sajid and  Pedro AM Mediano and  Karl Friston  [[bib]](bibtex.bib#L667-L674) 

 
## Acknowledgements 
 
Many thanks to @conorheins, Tomasz Korbak, Ryan Smith, Mel Andrews, Casper Hesp, and Manuel Baltieri for their helpful suggestions. 
 

 
## Contributing 
 
To contribute, please make pull requests adding entries to the bibtex file.  
 
 The README file was generated from bibtex using the `bibtex_to_md.py` file. 
 The keywords to use for each classification (Survey, Discrete-state-space etc) can be found at the bottom of the .py file. 

 
*This code and structure is heavily inspired by https://github.com/optimass/continual_learning_papers.*