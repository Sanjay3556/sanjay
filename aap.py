<!DOCTYPE html>
<html >
<!--From https://codepen.io/frytyler/pen/EGdtg-->
<head>
<title>Machine Learning Lab Experiment Deployment</title>
<meta charset="UTF-8">
<link href='https://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Arimo' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Hind:300' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>
 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous"> 
<style><!DOCTYPE html>

h1 {text-align: center;}
h2 {text-align: center;}
h3 {text-align: center;}
p {text-align: center;}
div {text-align: center;}
</style>
</head>

<body>
 
     
<div class="" style="background-color:blue;" >
<div class="clearfix">
           
<div class="col-md-12">
<center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
<center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
<center><p style="font-size:25px;color:white;margin-top:10px;">Summer internship project 4 Machine Learning Experiment Deployment</p></center> 
</div>
</div>
</div>

<div class="login">
<h2 >To predict whether person survived or not in Titanic Disaster</h2>
<h4>Developed by Sanjay Singh</h4>
<!-- Main Input For Receiving Query to our ML -->
<form action="{{ url_for('predict')}}"method="get">
<div class="form-floating mb-3">

<input type="number" class="form-control" id="pclass" name="pclass" step="any" min="1" max="3" placeholder="0" required="required">
<label for="floatingInput">Enter PClass Number</label>
</div>
<br>
<div class="form-floating mb-3">
<input type="number" class="form-control" id="age" name="age" step="any" min="0" max="100" placeholder="0" required="required">
<label for="floatingInput">Enter Age</label>
</div>
<br>
<div class="form-floating mb-3">
<input type="number" class="form-control" id="sibsp" name="sibsp" step="any" min="0" max="8" placeholder="0" required="required">
<label for="floatingInput">Enter SibSp Number</label>
</div>
<br>
<div class="form-floating mb-3">
<input type="number" class="form-control" id="parch" name="parch" step="any" min="0" max="6" placeholder="0" required="required">
<label for="floatingInput">Enter Parch Number</label>
</div>
<br>
<div class="form-floating mb-3">
<input type="number" class="form-control" id="sex" name="sex" step="any" min="0" max="1" placeholder="0" required="required">
<label for="floatingInput">Type "0" for "Male" or "1" for "Female"</label>
</div>
<br>
<div class="form-floating mb-3">
<input type="number" class="form-control" id="fare" name="fare" step="any" min="0" max="600" placeholder="0" required="required">
<label for="floatingInput">Enter Fare</label>
</div>
<br>

<br>
<button type="submit" class="btn btn-primary btn-block btn-large" value="rf" name="rf">Prediction by RandomForest Model</button>
<button type="submit" class="btn btn-primary btn-block btn-large" value="gb" name="gb">Prediction by GaussianNB Model</button>
</form>
<br>
<br>
{{ prediction_text }}

</div>

<div class="" style="background-color:blue;" >
<div class="clearfix">
           
<div class="col-md-12">
 <center><p style="font-size:25px;color:white;margin-top:20px;">Summer internship project 4 </p></center> 
</div>
</div>
</div>
</body>
</html>
