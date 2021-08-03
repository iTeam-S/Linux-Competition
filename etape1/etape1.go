package main
import "fmt"
import (
    "os/user"
	"vigenere"
)

func introduction(){
	fmt.Println("Bonjour! Bienvenue dans l'etape 1")
	fmt.Println("Theme: --> Qui suis-je ? <-- \n")
	fmt.Println("C'est de l'identité qu'est née la différence. Comme tous les choses, comme tous les objets chaque personne a une identité.\n\n")

	fmt.Println("Indice:\n Je suis une commande Unix, je ne comporte qu'au maximum 3 lettre,\n souvent utilisé pour pointer une indentité d'un objet, surtout connu dans les colonnes d'une base de données.")
}

func jeu(){
	user, err := user.Current()
    if err != nil {
        panic(err)
    }
	fmt.Println("Si vous traduiser le theme, en anglais, vous aurez surement une commande.\n")
	fmt.Print("Qui est-tu?: ")

	var user_tape string
	fmt.Scanln(&user_tape)

	if user_tape != user.Username {
		fmt.Println("\nOups, Je te connais pas!!!")
		return
	}
	fmt.Println("\nMais je connais beaucoup de", user.Username, "!")
	fmt.Print("Alors, qui est-tu vraiment ?: ")

	var id_tape string
	fmt.Scanln(&id_tape)

	if id_tape != user.Uid {
		fmt.Println("\n\nDésolé, Je ne peux pas t'identifier!!\nEtape echoué, tu peux toujours réessayer.")
		return
	}
	fmt.Println("Féliciation, tu as réusi l'etape 1")

	var nom_user string
	fmt.Println("Pour vérifier que tu as terminé l'etape, Je te donne une clé.")
	fmt.Print("Entre ton prenom: ")
	fmt.Scanln(&nom_user)

	encoded := vigenere.Encipher("ETAPEA", nom_user+"y")

	fmt.Println("Voici ta clé, pour la prochaine episode: ", encoded)
}

func main(){
	introduction()
	jeu()
}