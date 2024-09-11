@main
def main() =
  val person: Person = Person("Josh", 20)
  println(person.toString())

class Person(var name: String = "David", var age: Int = 21) {
  override def toString() =
    "Name: " + name + " || Age: " + age
}
