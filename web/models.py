from django.db import models
from django.core.exceptions import ValidationError

from utilisateur.models import Utilisateur
# Create your models here.
class Secteur(models.Model):
    codeSect=models.CharField(max_length=20,primary_key=True)
    secteur=models.CharField(max_length=50)
    
    def __str__(self):
        return self.secteur 

class Filiere(models.Model):
    codeF=models.CharField(max_length=20,primary_key=True)
    secteur=models.ForeignKey(Secteur,on_delete=models.CASCADE)
    filiere=models.CharField(max_length=50)
    
    def __str__(self):
        return self.filiere

class AnneeScolaire(models.Model):
    codeAS=models.AutoField(primary_key=True)
    annee_scolaire=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.annee_scolaire

class TypeFormation(models.Model):
    codeTF=models.CharField(max_length=20,primary_key=True)
    type_formation=models.CharField(max_length=100)
    
    def __str__(self):
        return self.type_formation
class Responsable(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom +" "+self.prenom

class Classe(models.Model):
    niveau=(
        ('1ere Année','1ere Année'),
        ('2eme Année','2eme Année'),
        ('Terminale','Terminale'),
    )
    type_formation= models.ForeignKey(TypeFormation,on_delete=models.CASCADE)
    codeC=models.CharField(max_length=20,primary_key=True)
    annee_scolaire=models.ForeignKey(AnneeScolaire,on_delete=models.CASCADE)
    filiere=models.ForeignKey(Filiere,on_delete=models.CASCADE)
    niveau=models.CharField(max_length=30,choices=niveau)
    responsable=models.ForeignKey(Responsable,on_delete=models.CASCADE)
    classe=models.CharField(max_length=50)

    def __str__(self):
        return self.classe

  
class Etudiant(models.Model):
    matricule=models.PositiveIntegerField(default=0)
    numero=models.PositiveIntegerField(default=0)
    sexechoix=(
        ('Feminin','Feminin'),
        ('Masculin','Masculin')
    )
    position=(
        ('P','Pasant(e)'),
        ('R','Redoublant(e)'),
        ('TRP','Tansfert Passant'),
        ('TRR','Transfert Redoublant')
    )
    position=models.CharField(max_length=100,choices=position)
    classe=models.ForeignKey(Classe,on_delete=models.CASCADE)
    sexe=models.CharField(max_length=20,choices=sexechoix)
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    date_de_naissance=models.DateField()
    lieu_de_naissance=models.CharField(max_length=100,blank=True, null=True)
    image=models.ImageField(upload_to="etudiant",blank=True, null=True)
    ecole_origine=models.CharField(max_length=50,blank=True, null=True)
    telephone=models.CharField(max_length=20,blank=True, null=True,default=None)
    email=models.EmailField(blank=True, null=True,default=None)
    adresse=models.CharField(max_length=120,blank=True, null=True,default=None)
    nom_du_pere=models.CharField(max_length=100,blank=True, null=True,default=None)
    profession_pere=models.CharField(max_length=70,blank=True, null=True,default=None)
    nom_de_la_mere=models.CharField(max_length=100,blank=True, null=True,default=None)
    profession_mere=models.CharField(max_length=70,blank=True, null=True,default=None)
    adresse_des_parents=models.CharField(max_length=100,blank=True, null=True,default=None)
    nom_du_correspondant=models.CharField(max_length=100,blank=True, null=True,default=None)
    profession_correspondant=models.CharField(max_length=70,blank=True, null=True,default=None)
    adresse_des_correspondant=models.CharField(max_length=100,blank=True, null=True,default=None)
    nombre_de_frere=models.PositiveIntegerField(default=0)
    nombre_de_soeur=models.PositiveIntegerField(default=0)
    rang_dans_la_famille=models.PositiveIntegerField(default=1,blank=True, null=True)
    sport_preferer=models.CharField(max_length=70,blank=True, null=True)
    sport_pratique=models.CharField(max_length=70,blank=True, null=True)
    date_joindre=models.DateField(auto_created=True,auto_now=True)
    
    def __str__(self):
        return self.prenom
    
class Periode(models.Model):
    codeP=models.AutoField(primary_key=True)
    periode=models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.periode

class TypeMatiere(models.Model):
    type_matiere=models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_matiere

class Matier(models.Model):
    matier=models.CharField(max_length=100)
    type_matiere=models.ForeignKey(TypeMatiere,on_delete=models.CASCADE)
    def __str__(self):
        return self.matier

class Matiere(models.Model):
    niveau=(
        ('1ere Année','1ere Année'),
        ('2eme Année','2eme Année'),
        ('Terminale','Terminale'),
    )
    filiere=models.ForeignKey(Filiere,on_delete=models.CASCADE)
    niveau=models.CharField(max_length=30,choices=niveau)
    matiere=models.ForeignKey(Matier,on_delete=models.CASCADE)
    coeff=models.PositiveIntegerField(default=1)
    class Meta:
        unique_together=[("filiere","niveau","matiere")]
    
    def __str__(self):
        return str(self.matiere.matier) +" "+"de"+ " "+ str(self.niveau) +" "+ str(self.filiere)
    
class Note(models.Model):
    annee_scolaire=models.ForeignKey(AnneeScolaire,on_delete=models.CASCADE)
    classe=models.ForeignKey(Classe,on_delete=models.CASCADE)
    periode=models.ForeignKey(Periode,on_delete=models.CASCADE)
    matiere=models.ForeignKey(Matiere,on_delete=models.CASCADE)
    utilisateur=models.ForeignKey(Utilisateur,on_delete=models.PROTECT,blank=True, null=True)
    etudiant=models.ManyToManyField(Etudiant,through="contenir")
    class Meta:
        unique_together=[("annee_scolaire","classe","periode","matiere")]
    
    def __str__(self):
        return f"NOTE" + " " +str(self.matiere.matiere) + " "+"PERIODE :"+" " +self.periode.periode+" "+"CLASSE :"+" "+ str(self.classe)
  
      
class Contenir(models.Model):
    note=models.ForeignKey(Note,on_delete=models.CASCADE)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    DS1=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    DS2=models.FloatField(blank=True, null=True,default=None)
    exam=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    class Meta:
        unique_together=[("note","etudiant")]
    
    def DS(self):
        if self.DS2== None:
            DS=self.DS1
        else:
           DS=(float(self.DS1) + (self.DS2))/2 
        return float(DS)
    def moyenne_par_matiere(self):
        return float( self.DS() + float(self.exam))/2
    def note_avec_coeff(self):
        return float((self.moyenne_par_matiere()) * self.note.matiere.coeff)
    
    def obs(self):
        a=self.moyenne_par_matiere()
        if a<10:
            b="faible"
        else:
            b="moyenne"
        return b

class Abs(models.Model):
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    periode=models.ForeignKey(Periode,on_delete=models.CASCADE)
    annee_scolaire=models.ForeignKey(AnneeScolaire,on_delete=models.CASCADE)
    nb_abscence=models.PositiveIntegerField(default=0)

    class Meta:
        unique_together=[("periode","etudiant","annee_scolaire")]
        
class SG(models.Model):
    sexechoix=(
        ('Feminin','Feminin'),
        ('Masculin','Masculin')
    )
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    sexe=models.CharField(max_length=20,choices=sexechoix)
    
    def __str__(self) -> str:
        return self.nom +" "+self.prenom

class ChefDeTravaux(models.Model):
    sexechoix=(
        ('Feminin','Feminin'),
        ('Masculin','Masculin')
    )
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    sexe=models.CharField(max_length=20,choices=sexechoix)
    
    def __str__(self) -> str:
        return self.nom +" "+self.prenom
    
class Censeur(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nom +" "+self.prenom

class Proviseur(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nom +" "+self.prenom