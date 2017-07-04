// a few tests for using JSON serialization

import org.scalatest.{FunSuite}

import org.json4s._
import org.json4s.jackson.JsonMethods._

class JsonSuite extends FunSuite {

  test("a newly created Person message has the expected fields") {
    val obj = parse(""" { "numbers" : [1, 2, 3, 4] } """)
    val exp = JObject(List(("numbers", JArray(List(JInt(1), JInt(2), JInt(3), JInt(4))))))
    assert(obj == exp)
  }

  test("some other fancy test")(pending)
}