@aging
Feature: BHMC_AgingTest
# 질문 : 여기 Feature는 어디서 쓴다고 했지?

  @A01.01.TestAging
  Scenario: AgingTest 시작하기
    Given A01.01 - USB 카메라와 Power 장비 및 ADB가 정상적으로 연결되어 있다.
    When A01.01 - 아래와 같은 Step으로 1시간 단위 Test를 수행하며, 이후 BAT off/ong 후 반복 수행하여 Memory 관련 문제가 없어야 한다.
    """
    BAT Off 동작을 5초 대기 시간으로 수행한다.
    BAT On 동작을  120초 대기 시간으로 수행한다. 이후 Refresh와 Home Screen으로 이동 동작 한다.
    Radio CH을 P1 > P2 > P3 > P1 동작을 20초 간격으로 10회 수행한다.(약 600초)
    '''
    Yendex Music을 play하고 10초 간격으로 Next Track곡을 80번 수행한다.(약 800초)
    BT Audio를 Play하고 20초 간격으로 Next Track곡을 45번 수행한다.(약 900초)
    Navigation 항목을 20초 대기 시간으로 5회 반복 진입한다.
    Radio 항목을 20초 대기 시간으로 진입한다.
    '''
    """
    Then A01.01 - Aging Test 완료 후 시료는 Radio 항목으로 진입 후, 문제없이 동작되어야 한다.