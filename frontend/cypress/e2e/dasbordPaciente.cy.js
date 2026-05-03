it("deve exibir informações principais do usuário", () => {
  cy.visit("/dashboard-paciente");

  cy.contains("Próximas Consultas").should("exist");
  cy.contains("Agendar Nova Consulta").should("exist");
  cy.contains("Notificações").should("exist");
  cy.contains("Consultas Passadas").should("exist");
});

it("deve exibir botão de entrar nas próximas consultas", () => {
  cy.visit("/dashboard-paciente");

  cy.contains("Próximas Consultas");

  cy.contains("Dr. Carlos Mendes")
    .parent()
    cy.contains("Entrar").should("have.length.at.least", 1);
});