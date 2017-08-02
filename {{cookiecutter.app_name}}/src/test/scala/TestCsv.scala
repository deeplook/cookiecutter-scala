// a few tests for reading CSV files

import org.scalatest.{FunSuite}

import com.github.tototoshi.csv.CSVReader
import java.io.File

class CsvSuite extends FunSuite {

  test("a CSV file has the expected fields in the first data row") {
    val reader = CSVReader.open(new File("src/test/resources/airport-codes.csv"))
    val obj = reader.allWithHeaders()(0)("coordinates")
    val exp = "-74.93360138, 40.07080078"
    assert(obj == exp)
  }

  test("some other fancy test")(pending)
}



