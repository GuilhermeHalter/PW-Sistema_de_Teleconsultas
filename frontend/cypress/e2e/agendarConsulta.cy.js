it("deve filtrar por especialidade", () => {
  cy.visit("/agendamento-consulta");

  cy.get("select").select("Cardiologista");

  cy.contains("Cardiologista").should("exist");
});