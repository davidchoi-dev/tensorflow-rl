# 베이지안 추론(Bayesian Inference)

## 셜록 홈즈의 베이지안 추론

베이지안 추론에 적합한 짤방으로 베이지안 추론에 대한 이야기를 시작하겠습니다. 명탐정 코난은 상당히 많은 이야기과 아이디어를 소설 셜록홈즈에서 인용했습니다. 그리고, 우리의 주인공 코난은 셜록 홈즈의 명대사를 인용해서, 사건을 해결해나갑니다.

![conan](http://chris-chris.ai/img/bayesian/conan2.jpg)

![conan](http://chris-chris.ai/img/bayesian/conan3.jpg)

![conan](http://chris-chris.ai/img/bayesian/conan4.jpg)

[출처 : 239화, 명탐정 코난(애니메이션)]

![conan](http://chris-chris.ai/img/bayesian/holmes2.jpg)

"설령 믿어지지 않는다고 해도, 가능성을 제외하고 남는 게 진짜 범인이다."

셜록 홈즈의 이 멋진 명언은 베이지안 추론의 기본적인 개념을 잘 설명합니다. 우리에게 A, B, C, D라는 네 명의 용의자가 있다고 합시다. 단서를 하나 하나 발견할 때마다, 용의자가 진짜 범인일 확률이 줄어듭니다. 최초로 우리가 아무 단서가 없이 네 명의 용의자를 만났을 때 우리는 4명의 용의자가 범인이라고 믿는 확률이 동일합니다. 아무런 단서가 없을 때 각 용의자가 범인인 확률을 바로 사전확률 Prior 라고 합니다. 그리고 새로운 단서가 발견되었을 때 업데이트된 새로운 확률 분포를 바로 사후확률 Posterior라고 합니다.

![conan](http://chris-chris.ai/img/bayesian/conan5.png)

[출처 : p17, Doing Bayesian Data Analysis 2nd Edition, John K.KRUSCHKE]

* 1단계 : 아무 단서가 없는 상태다.

맨 처음에는 아무 단서가 없기 때문에 A, B, C, D 네 명의 용의자 모두 같은 확률로 범인일 가능성을 가지고 있습니다. 각 용의자가 범인일 확률은 25%입니다.

* 2단계 : 용의자 A가 확실한 알리바이가 있다. A는 범인일 확률이 없다.

용의자 A의 알리바이가 확인되었습니다. 이제, 남은 용의자는 B, C, D입니다. 용의자 A가 대상에서 제외되면서 나머지 용의자들이 범인일 확률이 조금씩 올랐습니다. B, C, D 용의자가 범인일 확률은 이제 약 33%입니다.

* 3단계 : 용의자 B가 확실한 알리바이가 있다. B는 범인일 확률이 없다.

용의자 B의 알리바이가 확인되었습니다. 이제, 남은 용의자는 C, D입니다. 용의자 A가 대상에서 제외되면서 나머지 용의자들이 범인일 확률이 조금씩 올랐습니다. C, D 용의자가 범인일 확률은 이제 약 50%입니다.

* 4단계 : 용의자 C가 확실한 알리바이가 있다. C는 범인일 확률이 없다.

용의자 C의 알리바이가 확인되었습니다. 이제, 남은 용의자는 D입니다. 용의자 C가 대상에서 제외되면서 이제 용의자는 단 한명 밖에 남지 않았습니다. D 용의자가 범인일 확률은 이제 100%입니다.

## 금발의 미녀

사실 현실 세계에서 발생하는 사건들을 위에서 들었던 예처럼 단순하지 않습니다. 조금만 더 복잡한 예를 들어보겠습니다. 당신은 금발의 긴 머리를 가진 사람이 티켓을 떨어뜨린 것을 발견했습니다. 그럼 여러분은 어떻게 반응해야 할까요?

![blonde](http://chris-chris.ai/img/bayesian/blonde.jpeg)

"저기요, 아저씨 티켓 떨어졌어요!"

"저기요, 아가씨 티켓 가져가세요!"

자..잠깐! 긴 금발 머리를 가진 경우, 남자일 확률과 여자일 확률은 각각 얼마가 될까요? 

![tok](http://chris-chris.ai/img/bayesian/tok.jpeg)

일단 긴머리라는 사실만으로는 상대방의 성별을 확신하기는 어렵습니다. 티켓을 찾아주기 전에 뭐라고 불러야 할지 상대방이 남자일지 여자일지 천천히 확률을 한번 계산해보겠습니다.

일단 주변을 둘러보니, 100명의 사람들이 있습니다. 100명의 사람들 중에 50명이 남자이고, 50명은 여자였습니다. 50명의 여자들 중에서 긴 머리의 여자는 25명이었고, 짧은 머리는 25명이었습니다. 남자의 경우 48명이 짧은 머리였고, 2명만이 긴 머리였습니다.

```
P(여자) 
= # 여자 / # 사람
= 50 / 100
= 0.5

P(남자)
= # 남자 / # 사람
= 50 / 100
= 0.5

P(긴머리, 여자)
= # 긴머리를 가진 여자 / # 여자
= 25 / 50
= 0.5

P(긴머리, 남자)
= P(긴머리, 남자) P(남자)
= # 긴머리를 가진 남자 / # 남자
= 2 / 50
= 0.04

P(긴머리 | 여자)
= P(긴머리, 여자) P(여자)
= 0.5 * 0.5
= 0.25

P(긴머리 | 남자)
= P(긴머리, 남자) P(남자)
= 0.04 * 0.5
= 0.02
```

우리가 아는 정보는 아직 위 정보들 밖에 없습니다. 하지만 우리가 알고자 하는 확률은 아래와 같습니다.

```
P(남자 | 긴머리) # 긴머리인 경우 남자일 확률
P(여자 | 긴머리) # 긴머리인 경우 여자일 확률
```

P(남자 | 긴머리) 이 정보를 얻으려면 우리는 베이즈 정리를 사용할 수 있습니다.

$$P(남자 | 긴머리) 
= \frac{P(긴머리 | 남자) P(남자)\ \ \ \ \ \ \ \ \ }{P(긴머리)}
= \frac{P(긴머리 | 남자) P(남자)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }{P(긴머리\ 남자) + P(긴머리\ 여자)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }
$$

$$
= \frac{0.04 * 0.5}{0.02 + 0.25}
= \frac{0.02}{0.27}
= 0.07
$$


## 같은 상황이지만 다른 장소

이번에도 마찬가지로 금발의 긴 머리를 가진 사람이 티켓을 떨어뜨렸습니다. 하지만, 이 곳은 여자가 그리 많지 않은 공학대학 식당입니다. 주변을 둘러보니, 100명의 사람들이 있습니다. 100명의 사람들 중에 98명이 남자이고, 2명은 여자였습니다. 2명의 여자들 중에서 긴 머리의 여자는 1명이었고, 짧은 머리는 1명이었습니다. 남자의 경우 94명이 짧은 머리였고, 4명만이 긴 머리였습니다.

이 상황에서도 티켓을 떨어뜨린 사람이 남자일 확률을 구해보겠습니다.

```
P(여자) 
= # 여자 / # 사람
= 2 / 100
= 0.02

P(남자)
= # 남자 / # 사람
= 98 / 100
= 0.98

P(긴머리, 여자)
= # 긴머리를 가진 여자 / # 여자
= 1 / 2
= 0.5

P(긴머리, 남자)
= P(긴머리, 남자) P(남자)
= # 긴머리를 가진 남자 / # 남자
= 4 / 98
= 0.04

P(긴머리 | 여자)
= P(긴머리, 여자) P(여자)
= 0.5 * 0.02
= 0.01

P(긴머리 | 남자)
= P(긴머리, 남자) P(남자)
= 0.04 * 0.98
= 0.04
```

$$
P(남자 | 긴머리) 
= \frac{P(긴머리 | 남자) P(남자)\ \ \ \ \ \ \ \ \ }{P(긴머리)}
= \frac{P(긴머리 | 남자) P(남자)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }{P(긴머리\ 남자) + P(긴머리\ 여자)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }


= \frac{0.04 * 0.98}{0.01 + 0.04}
= \frac{0.04}{0.05}
= 0.80
$$

슬프게도, 지금 주운 티켓의 주인은 남자일 확률이 80%입니다.

이와 같이, 여자가 긴 머리를 할 확률과 남자가 긴 머리를 할 확률이 비슷할 지라도, 주변에 있는 남자와 여자의 사람 수가 많은 영향을 미치는 것을 확인할 수 있습니다.




베이지안 추론 (Bayesian inference)은 베이즈 정리 (Bayes 's theorem)를 사용하여 더 많은 증거 또는 정보를 얻을 수있을 때 가설 확률을 업데이트하는 통계적 추론 방법입니다. 베이지안 추론은 통계, 특히 수학 통계에서 중요한 기술입니다. 베이지안 업데이트는 일련의 데이터를 동적으로 분석 할 때 특히 중요합니다. 베이지안 추론은 과학, 공학, 철학, 의학, 스포츠, 법학 등 다양한 활동에 적용됩니다. 의사 결정 이론의 철학에서 베이지안 추론은 종종 "베이지안 확률 (Bayesian probability)"이라고 불리는 주관적인 확률과 밀접하게 관련되어 있습니다.

Formal
베이지안 추론은 두 가지 전제의 결과 인 사후 확률, 사전 확률 및 관측 된 데이터에 대한 통계 모델로부터 유도 된 "우도 함수"를 도출합니다. 베이지안 추론은 베이 즈 정리에 따라 사후 확률을 계산합니다.

$$P(H\mid E)={\frac {P(E\mid H)\cdot P(H)}{P(E)}}$$

where

$$\textstyle \mid \ means "event\ conditional\ on" (so\ that\ {\displaystyle \textstyle (A\mid B)}\ means\ A\ given\ B).$$

$ H $는 확률이 데이터에 의해 영향을받을 수있는 가설을 나타냅니다 (아래 증거 참조). 종종 경쟁하는 가설들이 있으며, 그 중 가장 가능성이 높은 것을 결정하는 것이 과제입니다.
그 증거

$ E $는 이전 확률 계산에 사용되지 않은 새 데이터에 해당합니다.
사전 확률 인 $ P (H) $는 현재 증거 인 데이터 $ E $가 가설 전에 가설 $ H $의 확률의 추정치입니다.

$$ P (H \mid E) $$는 사후 확률로서 $$ H $$가 주어 졌을 때, 즉 $$ E $$가 관찰 된 후에 발생합니다. 이것은 우리가 알고 자하는 것입니다 : 관찰 된 증거가 주어진 가설의 확률.

$$ P (E \mid H) $$는 $$ H $$ 주어진 $$ E $$를 관찰 할 확률입니다. $$ H $$를 고정시킨 $$ E $$의 함수로서, 이것은 확률입니다. 이것은 주어진 가설과 증거의 호환성을 나타냅니다. 우도 함수는 증거의 함수, $$ E $$이고, 사후 확률은 가설의 함수이며 $$ H $$이다.

$$ P (E) $$는 때때로 한계 가능성 (marginal likelihood) 또는 "모형 증거"라고 불린다. 이 요인은 고려되는 모든 가능한 가설에 대해 동일합니다 (다른 모든 요인과 달리 가설 $ H $이 기호의 어느 곳에서도 나타나지 않는다는 사실에서 명백한 것처럼). 따라서이 요소는 상대적인 요소를 결정하지 않습니다 다른 가설의 확률.

$ H $의 다른 값에 대해, 분자의 두 요소 모두 $$ P (H) $$와 $$ P (E \mid H) $$만이 $$ P (H \mid E) $$의 값에 영향을줍니다. 가설의 이전 확률 (고유 한 확률)과 새로 획득 된 우도 (새로운 관측 된 증거와의 호환성)에 비례한다.

Bayes의 규칙은 다음과 같이 작성할 수도 있습니다.

$$P(H\mid E)={\frac {P(E\mid H)}{P(E)}}\cdot P(H)$$

여기에서 $${\frac {P(E\mid H)}{P(E)}}$$는 $$ H $$의 확률에 $$ E $$의 영향으로 해석 될 수 있습니다