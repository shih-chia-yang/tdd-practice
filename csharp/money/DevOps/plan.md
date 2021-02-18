# plan

- [ ]實驗分支策略，當新需求發生時，以分支命名，完成功能後個人端使用rebase squash整理成一個commit，再merge squash至master
  -[x] #tags refact/refactor-exchange-entity  add new git branch
    - [ ] #tags refact/refactor-exchange-entity renamed ExchangeService
    - [ ] #tags refact/refactor-exchange-entity add IExchangeService and design method
    - [ ] #tags refact/refactor-exchange-entity bank add constructor,and injected IExchangeService