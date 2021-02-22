# plan

- [ ]實驗分支策略，當新需求發生時，以分支命名，完成功能後個人端使用rebase squash整理成一個commit，再merge squash至master
  - [x] 是否需更新遠端分支
    - [x]目前作業會上傳，並且使用pull request  
  - [ ] rebase squash使用於本地分支修改commit，當工作事項完成後使用merge squash
    - [x] 使用 merge squash，但不熟悉github pull request，完成pull request後又產生一個commit，似乎應該完成工作後發出pull request，由github完成，不建議直接使用指令merge
- [ ] #tags work-item
  - [x] #tags refact/refactor-exchange-entity  add new git branch [[refactor-exchange-entity.md]]
  - [x] #tags refact/refactor-Money-valueobject add new git branch [[refactor-Money-valueobject.md]]
  - [x] #tags refact/refactor-ExchangeService [[refactor-exchange-service.md]]
    - [x] add new git branch 
  - [x] #tags refact/refactor-pair-valueobject [[refactor-pair-vauleobject.md]]
    - [x] add new git branch
    - [x] add md file
  - [x] #tags test/clean-repeat-test-method [[test-clean-repeat-test-methods.md]]
    - [x] add new git branch
    - [x] add md file
  - [ ] #tags design validation object
    - [ ] #tags feat/add-validation-object
    - [ ] add new git branch
    - [ ] add md file