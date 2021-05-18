# Competition 2: dynamic pricing 

In this competition, you must write an algorithm that can set prices in dynamic competition against one opponent. 

In order to have the correct version of `game_tournament` consider starting with 
``bash
pip install git+https://github.com/GamEconCph/game-tournament
``


The relevant information to your player comes as: 

* `state['payoffs']`: list of profit functions of the form `demand(p1, p2, 0) * (p1 - c)`
* `state['actions']`: list of tuples, `(pmin, pmax)`, denoting the interval of allowed prices (end points included). 
* `state['discount_factor']`: value of 1$ tomorrow in today's terms 
* `state['marginal_cost']`: common marginal cost (scalar). (baked into the payoff function)
* `history`: list of 2-vectors of previous actions. E.g. `history[-1]` gives a 2-vector of the prices in previous period. 
​
When working with the demand function, note that the syntax is `demand(p1, p2, i)`. However, you have to infer which player your function is, so you need an exception like the following code block, which best responds to an opponent price of 1.0: 

``python
i = self.i # read from your player's property (will be assigned at runtime)
pj = 1.0 # keeping opponent price fixed at some value 
if i == 0: 
    fun = lambda p : -payoff(p, pj, i)
else: 
    fun = lambda p : -payoff(pj, p, i)
res = minimize(fun, x0=pj)
p = res.x
return p
``