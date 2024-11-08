#include <fstream>
#include <iostream>
#include <string>
using namespace std;
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class Ville {
  private:
    string nom;
    int code_postal;
    int prix_metre2;

  public:
    Ville(string nom_, int code_postal_, int prix_metre2_)
        : nom{nom_}, code_postal{code_postal_}, prix_metre2{prix_metre2_} {}
    friend std::ostream& operator<<(std::ostream& out, const Ville& v) {
      return out << v.nom << " ; Code postale: " << v.code_postal
                << " ; Prix par m2: " << v.prix_metre2;
    }
    Ville(json data) {
      nom = data["nom"];
      code_postal = data["code postale"];
      prix_metre2 = data["prix par m2"];
    }
    static void affichage(){
      while(true){
        static unsigned int id = 1;
        string url_ville = "http://localhost:8000/Ville/"+to_string(id);
        auto response = cpr::Get(cpr::Url{url_ville});
        if (response.status_code != 200) {
          break; // Arreter boucle si ID existe pas
        }
        const auto ville_ = Ville(
            json::parse(cpr::Get(cpr::Url{url_ville}).text));
        std::cout << "Ville: " << ville_ << "\n" << std::endl;
        id++;
      }
    }
};

class Local {
  protected: 
    string nom;
    std::unique_ptr<Ville> ville;
    int surface;

  public:
    Local(string nom_, json ville_, int surface_)
        : nom{nom_}, ville{std::make_unique<Ville>(ville_)}, surface{surface_} {}

    friend std::ostream& operator<<(std::ostream& out, const Local& l) {
      return out << l.nom << " ; Ville: " << *l.ville
                << " ; Surface: " << l.surface;
    }

    Local(json data) {
      nom = data["nom"];
      ville = make_unique<Ville>(data["ville"]);
      surface = data["surface"];
    }

    static void affichage(){
      while(true){
        static unsigned int id = 1;
        string url_local = "http://localhost:8000/Local/"+to_string(id);
        auto response = cpr::Get(cpr::Url{url_local});
        if (response.status_code != 200) {
          break;
        }
        const auto local_ = Local(
            json::parse(cpr::Get(cpr::Url{url_local}).text));
        std::cout << "Local: " << local_ << "\n" << std::endl;
        id++;
      }
    }
};

class SiegeSocial : Local {

  public:
    SiegeSocial(string nom_, json ville_, int surface_)
        : Local(nom_, ville_, surface_) {}
        
    friend std::ostream& operator<<(std::ostream& out, const SiegeSocial& ss) {
      return out << ss.nom << " ; Ville: " << *ss.ville
                << " ; Surface: " << ss.surface;
    }

    SiegeSocial(json data) : Local(data) {}

    static void affichage(){
      while(true){
        static unsigned int id = 1;
        string url_siege = "http://localhost:8000/siegesocial/"+to_string(id);
        auto response = cpr::Get(cpr::Url{url_siege});
        if (response.status_code != 200) {
          break; // Arreter boucle si ID existe pas
        }
        const auto siege = SiegeSocial(
            json::parse(cpr::Get(cpr::Url{url_siege}).text));
        std::cout << "Siege Social: " << siege << "\n" << std::endl;
        id++;
      }
    }
};

class Machine {
  private:
    string nom;
    int prix;
    int n_serie;

  public:
    Machine(string nom_, int prix_, int n_serie_)
        : nom{nom_}, prix{prix_}, n_serie{n_serie_} {}

    friend std::ostream& operator<<(std::ostream& out, const Machine& mach) {
      return out << mach.nom << " ; Prix: " << mach.prix
                << " ; Numero de serie: " << mach.n_serie;
    }

    Machine(json data) {
      nom = data["nom"];
      prix = data["prix"];
      n_serie = data["numero de serie"];
    }

    static void affichage(){
      while(true){
        static unsigned int id = 1;
        string url_machine = "http://localhost:8000/Machine/"+to_string(id);
        auto response = cpr::Get(cpr::Url{url_machine});
        if (response.status_code != 200) {
          break; // Arreter boucle si ID existe pas
        }
        const auto machine_ = Machine(
            json::parse(cpr::Get(cpr::Url{url_machine}).text));
        std::cout << "Machine: " << machine_ << "\n" << std::endl;
        id++;
      }
    }
};

class Objet {
  private :
    string nom;
    int prix;

  public:
    Objet(string nom_, int prix_)
        : nom{nom_}, prix{prix_} {}

    friend std::ostream& operator<<(std::ostream& out, const Objet& obj) {
      return out << obj.nom << " ; Prix: " << obj.prix;
    }

    Objet(json data) {
      nom = data["nom"];
      prix = data["prix"];
    }

    static void affichage(){
      while(true){
        static unsigned int id = 1;
        string url_objet = "http://localhost:8000/Objet/"+to_string(id);
        auto response = cpr::Get(cpr::Url{url_objet});
        if (response.status_code != 200) {
          break; // Arreter boucle si ID existe pas
        }
        const auto objet_ = Objet(
            json::parse(cpr::Get(cpr::Url{url_objet}).text));
        std::cout << "Objet: " << objet_ << "\n" << std::endl;
        id++;
      }
    }
};

auto main() -> int {
  std::cout << "\nAffichage Villes: \n"<< endl;
  Ville::affichage();
  
  std::cout << "\nAffichage Locals: \n"<< endl;
  Local::affichage();

  std::cout << "\nAffichage Machine: \n"<< endl;
  Machine::affichage();

  std::cout << "\nAffichage Objet: \n"<< endl;
  Objet::affichage();
  
  
  return 0;
}
