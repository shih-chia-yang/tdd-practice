#結合2個陣列物件，結合時以最短物件長度為準，超過捨棄
#使用時需確認2組物件長度相等
suits=["hearts","spades","clubs","diamonds"]
ranks=["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]

cards=zip(suits,ranks)
print(list(cards))

