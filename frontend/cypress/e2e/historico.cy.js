describe("Histórico de Consultas", () => {
  it("deve exibir as consultas", () => {
    cy.visit("/historico-consultas");

    cy.contains("Histórico de Consultas");
    cy.contains("Dr. Carlos Mendes");
    cy.contains("Dra. Mariana Costa");
  });
});


it("deve filtrar consultas agendadas", () => {
  cy.visit("/historico-consultas");

  cy.contains("Agendadas").click();

  cy.contains("Agendada");
});


it("deve exibir botão de entrar na consulta", () => {
  cy.visit("/historico-consultas");

  cy.contains("Entrar na Consulta").should("exist");
});

it("deve navegar para a página de perfil", () => {
  cy.visit("/historico-consultas");

  cy.contains("Perfil").click();

  cy.url().should("include", "/perfil");
  cy.contains("Meu Perfil");
});