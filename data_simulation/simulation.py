from kineuron import (TransitionState,
                      Transition,
                      RateConstant,
                      KineticModel,
                      Solver,
                      Stimulation)

model = KineticModel()

docked = TransitionState(name="Docked")
pprimed = TransitionState(name="pPrimed")
primed = TransitionState(name="Primed")
fusion = TransitionState(name="Fusion")


alpha = RateConstant(name="α", value=0.3, calcium_dependent=True)
beta = RateConstant(name="β", value=50.0*0.3)
rho = RateConstant(name="ρ", value=1.0)


t1 = Transition(name="Transition 1",
                rate_constant=alpha,
                origin="Docked",
                destination="pPrimed")

t2 = Transition(name="Transition 2",
                rate_constant=beta,
                origin="pPrimed",
                destination="Docked")

t3 = Transition(name="Transition 3",
                rate_constant=alpha,
                origin="pPrimed",
                destination="Primed")

t4 = Transition(name="Transition 4",
                rate_constant=beta,
                origin="Primed",
                destination="pPrimed")

t5 = Transition(name="Transition 5",
                rate_constant=alpha,
                origin="Primed",
                destination="Fusion")

t6 = Transition(name="Transition 6",
                rate_constant=rho,
                origin="Fusion",
                destination="Docked")

model.add_transition_states([docked, pprimed, primed, fusion])
model.add_transitions([t1, t2, t3, t4, t5, t6])

model.init()

stimulation = Stimulation(time_start_stimulation=0.1,
                          conditional_stimuli=3,
                          period=0.03,
                          tau_stimulus=0.0015,
                          intensity_stimulus=500,
                          time_wait_test=0.3)

experimento = Solver(model=model, stimulation=stimulation)

experimento.resting_state()

experimento.run(repeat=100, save_transitions=["Transition 5"])

resultados = experimento.get_results(mean=True)

resultados.to_csv("experimento.csv", index=True)
