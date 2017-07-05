# Cookiecutter Scala

This is a template for [Cookiecutter](https://github.com/audreyr/cookiecutter), a tool that creates projects from project templates. Using this template you can create a working project skeleton for a simple hello world-like Scala project, with some additional bells and whistles, if needed, like:

- [sbt](https://github.com/sbt/sbt) to build the project
- [scalatest](https://github.com/scalatest/scalatest) to test the code
- [Apache Toree](https://toree.incubator.apache.org/) to explore the code interactively in a notebook
- [scoverage](https://github.com/scoverage/sbt-scoverage) to create code coverage reports (optional)
- [scalariform](https://github.com/scala-ide/scalariform) to format the code (optional)
- [json4s](https://github.com/json4s/json4s) to use JSON (optional)
- [scalapb](https://github.com/scalapb/ScalaPB) to read/write Protobuf messages (optional)

Most of these are optional and will be added to a newly created project only when provinding a version number other than `-` for the respective library during project instantiation. The default version numbers are the most recent ones, but are hardwired and not dynamically looked up.


## Generate a project skeleton

- install cookiecutter, see [documentation](http://cookiecutter.readthedocs.io/en/latest/installation.html)
- run `cookiecutter https://github.com/deeplook/cookiecutter-scala.git`


## Sample project

A minimal version using only default version numbers and no optional libraries looks like this:

```bash
$ cookiecutter https://github.com/deeplook/cookiecutter-scala.git
app_name [hello-world]:
app_slug [hello_world]:
app_version [0.1.0]:
package_name [org.cookiecutter.scala.hello_world]:
sbt_version [0.13.15]:
scala_version [2.12.2]:
scalatest_version [3.0.1]:
scoverage_version [1.5.0]: -
json4s_version [3.5.2]: -
sbt_scalariform_version [1.6.0]: -
sbt_protoc_version [0.99.8]: -
scalapb_compilerplugin_version [0.6.0]: -

$ tree hello-world/
hello-world/
├── .gitignore
├── .travis
├── README.md
├── build.sbt
├── project
│   ├── build.properties
│   └── plugins.sbt
└── src
    ├── main
    │   └── scala
    │       └── Main.scala
    └── test
        └── scala
            └── MainSpec.scala
```

A maximal version using only default version numbers, also for all optional libraries, looks like this:

```bash
$ cookiecutter https://github.com/deeplook/cookiecutter-scala.git
app_name [hello-world]:
app_slug [hello_world]:
app_version [0.1.0]:
package_name [org.cookiecutter.scala.hello_world]:
sbt_version [0.13.15]:
scala_version [2.12.2]:
scalatest_version [3.0.1]:
scoverage_version [1.5.0]:
json4s_version [3.5.2]:
sbt_scalariform_version [1.6.0]:
sbt_protoc_version [0.99.8]:
scalapb_compilerplugin_version [0.6.0]:

$ tree hello-world/
hello-world/
├── .gitignore
├── .travis
├── README.md
├── build.sbt
├── project
│   ├── build.properties
│   ├── plugins.sbt
│   ├── project
│   └── scalapb.sbt
└── src
    ├── main
    │   ├── protobuf
    │   │   └── person.proto
    │   └── scala
    │       └── Main.scala
    └── test
        └── scala
            ├── MainSpec.scala
            ├── TestJson.scala
            └── TestProtobuf.scala
```


## Verify the generated project

For a sample project named `hello_world` using all optional libraries you can test your newly created project running this sequence of `sbt` commands (output heavily trimmed):

```bash
$ cd hello_world
$ sbt compile
...
[success] Total time: 11 s, completed Jul 4, 2017 10:47:55 AM

$ sbt run
...
[info] Running org.cookiecutter.scala.hello_world.Main
Hello World
[success] Total time: 6 s, completed Jul 4, 2017 10:48:49 AM

$ sbt test
...
[info] Run completed in 555 milliseconds.
[info] Total number of tests run: 5
[info] Suites: completed 3, aborted 0
[info] Tests: succeeded 5, failed 0, canceled 0, ignored 0, pending 2
[info] All tests passed.
[success] Total time: 7 s, completed Jul 4, 2017 10:49:29 AM

$ sbt doc
...
[info] Main Scala API documentation to /[...]/hello-world/target/scala-2.12/api...
model contains 11 documentable templates
[info] Main Scala API documentation successful.
[success] Total time: 4 s, completed Jul 4, 2017 10:50:33 AM

$ sbt clean coverage test
...
[info] [info] Beginning coverage instrumentation
[info] [info] Instrumentation completed [130 statements]
[info] [info] Wrote instrumentation file [/[...]/hello-world/target/scala-2.12/scoverage-data/scoverage.coverage.xml]
[info] [info] Will write measurement data to [/[...]/hello-world/target/scala-2.12/scoverage-data]
...
[info] All tests passed.
[success] Total time: 12 s, completed Jul 4, 2017 10:52:00 AM

$ sbt coverageReport
...
[info] Generating scoverage reports...
[info] Written Cobertura report [/[...]/hello-world/target/scala-2.12/coverage-report/cobertura.xml]
[info] Written XML coverage report [/[...]/hello-world/target/scala-2.12/scoverage-report/scoverage.xml]
[info] Written HTML coverage report [/[...]/hello-world/target/scala-2.12/scoverage-report/index.html]
[info] Statement coverage.: 30.00%
[info] Branch coverage....: 62.50%
[info] Coverage reports completed
[info] All done. Coverage was [30.00%]
[success] Total time: 2 s, completed Jul 4, 2017 10:53:15 AM
```

```bash
$ sbt console
...

// main functionality

scala> import org.cookiecutter.scala.hello.Main
import org.cookiecutter.scala.hello.Main

scala> Main.main(Array())
Hello World

// protobuf

scala> import person.Person
import person.Person

scala> val p = Person(name=Some(“Joe”))
p: person.Person =
name: “Joe”

// json

scala> import org.json4s._
import org.json4s._

scala> import org.json4s.jackson.JsonMethods._
import org.json4s.jackson.JsonMethods._

scala> val obj = parse(""" { "numbers" : [1, 2, 3, 4] } """)
obj: org.json4s.JValue = JObject(List((numbers,JArray(List(JInt(1), JInt(2), JInt(3), JInt(4))))))
```

This should give you a fully functional SBT-based Scala project, with some additional useful goodies if you like, that you can further modify according to your needs.
