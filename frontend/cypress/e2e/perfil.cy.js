describe("Perfil do Paciente", () => {
  it("deve exibir os dados do usuário", () => {
    cy.visit("/perfil");

    cy.contains("Maria Silva");
    cy.get('input').should("exist");
  });
});

it("deve permitir editar o nome", () => {
  cy.visit("/perfil");

  cy.get('input').first().clear().type("João Silva");

  cy.get('input').first().should("have.value", "João Silva");
});

it("deve alterar preferências de notificação", () => {
  cy.visit("/perfil");

  cy.get('input[type="checkbox"]').first().click();

  cy.get('input[type="checkbox"]').first().should("not.be.checked");
});

it("deve clicar no botão salvar", () => {
  cy.visit("/perfil");

  cy.contains("Salvar Alterações").click();
});