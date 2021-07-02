Feature: Cotizar seguro de hogar

  @cotizar
  Scenario: Cotizar seguro de hogar
    Given el usuario se encuentra en el home
    When ingresa a la sección: Personas - Seguros
    And ingresa al seguro de Hogar
    And realiza una cotización con la siguiente información
    | filter           | value          |
    | nombre           | Diego Castillo |
    | telefono         | 1135755555     |
    | correo           | test@test.com  |
    | tipo de vivienda | casa           |
    | superficie       | 30 a 40 m2     |
    | ubicacion        | CABA           |
    Then obtengo las cotizaciones
    And el valor mensual es positivo y entero
    And se visualiza el chat online