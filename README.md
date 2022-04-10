# prescriptionsRestApi

<b>Para rodar a aplicação no localhost </b>: <br>
   1 - Clonar repositório <br>
   Na linha de comando no diretório: <br>
   2 - pip install -r requirements.txt <br>
   3 - python app.py <br>
  
  
<h2> Documentação </h2>
<p> Optei por usar o framework FastApi, pois não tenho experiência em Django e me pareceu prover um desenvolvimento mais rápido em comparação.</p>

<p> As classes definidas no arquivo app.py Prescriptions, Metrics, Clinic, Patient e Physician herdam a classe BaseModel, que provê funcionalidades como validações de tipo de dados e geração automática de Json./p>
<p> Também disponibiliza decorators para routing e HTTP METHODS, permitindo a abstração do request. Para este teste, implementei o método add_prescription. </p>
<p> O método utiliza dos métodos valida() das classes criadas em Services.py, que consomem os endpoints e validam a resposta. </p>



  
  
 
 
