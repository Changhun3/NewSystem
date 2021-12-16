@aging
Feature: Avtovaz_AgingTest

  @A01.01.TestAging
  Scenario: AgingTest 시작하기
    Given A01.01 - USB 카메라와 Power 장비 및 ADB가 정상적으로 연결되어 있다.
    When A01.01 - 아래와 같은 Step으로 24 시간 동안 Aging Test를 수행하며, 동작중 Reboot 또는 crash 이슈는 없어야 한다.
    """
    BAT Off 동작을 5초 대기 시간으로 수행한다.
    BAT On 동작을  120초 대기 시간으로 수행한다.
    Radio CH을 1 > 2 > 3 > 1 동작을 40초 간격으로 수행한다.
    Yandex 음악을 910초 대기 시간으로 수행한다.
    BT Audio Play를 910초 대기 시간으로 수행한다.
    Navigation 항목을 20초 대기 시간으로 진입한다.
    Radio 항목을 20초 대기 시간으로 진입한다.
    """
    Then A01.01 - Aging Test 완료 후 시료는 Radio 항목으로 진입 후, 문제없이 동작되어야 한다.