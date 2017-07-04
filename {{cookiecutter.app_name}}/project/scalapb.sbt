addSbtPlugin("com.thesamet" % "sbt-protoc" % "{{ cookiecutter.sbt_protoc_version }}")

libraryDependencies += "com.trueaccord.scalapb" %% "compilerplugin" % "{{cookiecutter.scalapb_compilerplugin_version }}"
