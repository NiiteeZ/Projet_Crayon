#include <fstream>
#include <iostream>
#include <string>
using namespace std;
#include <cpr/cpr.h>

#include <nlohmann/json.hpp>
using json = nlohmann::json;

class Ville {
  string nom;
  int code_postal;
  int prix_metre2;

 public:
  Ville(string nom_, int code_postal_, int prix_metre2_)
      : nom{nom_}, code_postal{code_postal_}, prix_metre2{prix_metre2_} {}
  friend std::ostream& operator<<(std::ostream& out, const Ville& v) {
    return out << v.nom << " ; code postale: " << v.code_postal
               << " ; prix par m2: " << v.prix_metre2;
  }
  Ville(json data) {
    nom = data["nom"];
    code_postal = data["code postale"];
    prix_metre2 = data["prix par m2"];
  }
};

class Local {
  string nom;
  std::unique_ptr<Ville> ville;
  int surface;

 public:
  Local(string nom_, json ville_, int surface_)
      : nom{nom_}, ville{std::make_unique<Ville>(ville_)}, surface{surface_} {}
  friend std::ostream& operator<<(std::ostream& out, const Local& l) {
    return out << l.nom << " ; ville: " << *l.ville
               << " ; surface: " << l.surface;
  }
  Local(json data) {
    nom = data["nom"];
    ville = make_unique<Ville>(data["ville"]);
    surface = data["surface"];
  }
};

auto main() -> int {
  string urls1 = "http://localhost:8000/Ville/2";
  json data = json::parse(cpr::Get(cpr::Url{urls1}).text);

  const auto v = Ville(data);
  const auto l = Local(
      json::parse(cpr::Get(cpr::Url{"http://localhost:8000/Local/2"}).text));
  std::cout << "Local: " << l << std::endl;
  return 0;
}
