{% if cookiecutter.sbt_protoc_version != '-' %}
PB.targets in Compile := Seq(
  scalapb.gen() -> (sourceManaged in Compile).value
)
{% endif %}

lazy val root = (project in file(".")).
  settings(
    name := "{{ cookiecutter.app_name }}",
    version := "{{ cookiecutter.app_version }}",
    scalaVersion := "{{ cookiecutter.scala_version }}",
    libraryDependencies ++= Seq(
    {% if cookiecutter.json4s_version != '-' %}
      "org.json4s" %% "json4s-jackson" % "{{ cookiecutter.json4s_version }}",
      "org.json4s" %% "json4s-ext" % "{{ cookiecutter.json4s_version }}",
    {% endif %}
      "org.scalatest" %% "scalatest" % "{{ cookiecutter.scalatest_version }}" % "test"
    )
  )
