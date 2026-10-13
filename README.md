# VTAL Unidades — banco Neon + hospedagem Vercel

```
index.html     ← o site inteiro (HTML + CSS + JS num arquivo só)
api/rpc.js     ← a API: única parte que fala com o banco e confere as permissões
db/setup.sql   ← cria as tabelas e o administrador no Neon
server.mjs     ← só para testar no seu computador (a Vercel não usa)
front/         ← partes do index.html separadas (para editar com calma; rode `python3 build.py` para juntar)
```

Por que existe a pasta `api/`? Se o `index.html` falasse direto com o Neon, a senha do banco ficaria
dentro do arquivo e qualquer pessoa que abrisse o site poderia ler, alterar ou apagar tudo.
A API guarda a senha do banco na Vercel (variável de ambiente) e só devolve a cada usuário o que ele pode ver.

---

## 1. Criar o banco no Neon (5 min)

1. Entre em **neon.com** → **New project**.
   - Nome: `vtal-unidades`
   - Região: **AWS South America East 1 (São Paulo)**
2. No menu do projeto, abra **SQL Editor**.
3. Abra o arquivo `db/setup.sql`, copie **tudo** e cole no editor.
4. No final do texto, troque **nome, e-mail e senha** do administrador.
5. Clique em **Run**. Pronto: tabelas criadas e você já tem login de admin.
6. Clique em **Connect** (canto superior), deixe ligada a opção **Connection pooling** e copie a *connection string*
   (`postgresql://neondb_owner:...@ep-...-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require`).
   Guarde — ela é a senha do banco, **não compartilhe**.

> Não existe tela de "criar administrador" no site. O primeiro admin só nasce pelo SQL acima;
> os demais usuários você cria pelo próprio site, em **Usuários**.

## 2. Publicar na Vercel (5 min)

1. Crie um repositório **privado** no GitHub e envie esta pasta inteira.
2. Em **vercel.com** → *Add New → Project* → importe o repositório.
   - Framework Preset: **Other** · Build Command: deixe vazio.
3. Antes de clicar em Deploy, abra **Environment Variables** e adicione:
   | Nome | Valor |
   |---|---|
   | `DATABASE_URL` | a connection string do Neon (passo 1.6) |
   | `AUTH_SECRET` | um texto aleatório com 40+ caracteres (gere em https://generate-secret.vercel.app/64) |
4. **Deploy**. Abra o endereço gerado, entre com o admin e vá em **Importar / backup** para subir a planilha.

Se mudar alguma variável depois, faça *Redeploy* para valer.

## 3. Testar no seu computador (opcional)

Precisa do Node 20+.

```bash
npm install
cp .env.example .env      # cole DATABASE_URL e AUTH_SECRET
npm run dev               # abre em http://localhost:3000
```

## Segurança

- Senhas de login guardadas com bcrypt; 5 tentativas erradas bloqueiam o usuário por 15 min.
- Sessão em cookie `HttpOnly` assinado (12 h). Desativar um usuário ou redefinir a senha dele derruba a sessão na hora.
- UFs, permissões (ver / incluir / editar / excluir / ver senhas / exportar) e área de admin são conferidas **na API**.
  Quem não tem "ver senhas" não recebe as senhas nem na resposta do servidor.
- O Neon guarda o histórico do banco e permite restaurar para um momento anterior (*Backup & Restore* no painel do Neon).
