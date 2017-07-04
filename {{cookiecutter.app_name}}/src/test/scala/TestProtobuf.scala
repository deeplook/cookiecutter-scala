// a few tests for using protobuf serialization

import org.scalatest.{FunSuite}

import person.Person

class ProtobufSuite extends FunSuite {

  test("a newly created Person message has the expected fields") {
    val p = Person(name=Some("Bob"), age=Some(32))
    assert(p.getName == "Bob")
    assert(p.getAge == 32)
  }

  test("a Person can be recreated from a byte array it's been serialized to") {
    val p = Person(name=Some("Bob"), age=Some(32))
    val ba = p.toByteArray
    val q = Person.parseFrom(ba)
    assert(q == p)
  }

  test("some other fancy test")(pending)
}