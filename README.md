# prescriptionsRestApi

<b>Para rodar a aplicação no localhost </b>: <br>
<ol>
   <li> Clonar repositório </li>
   <span> Na linha de comando dentro do diretório: </span><br>
   <li>  pip install -r requirements.txt </li>
   <li>  python app.py </li>
   </ol>
  
  
<h2> Documentação </h2>
<p> Optei por usar o FastApi, pois  me pareceu prover um desenvolvimento mais rápido em comparação com outros frameworks.</p>

<p> As classes definidas no arquivo app.py Prescriptions, Metrics, Clinic, Patient e Physician herdam a classe BaseModel, que provê funcionalidades como validações de tipo de dados e geração automática de Json./p>
<p> Também disponibiliza decorators para routing e HTTP METHODS, permitindo a abstração do request. Para este teste, implementei o método add_prescription. </p>
<p> O método utiliza dos métodos valida() das classes criadas em Services.py, que consomem os endpoints e validam a resposta. </p>


<h3> To Do </hr>
<ul>
   <li> Unit Tests </li>
   <li> Deploy Heroku </li>
  </ul>



  
  
 
 
