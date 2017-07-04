resolvers += Resolver.typesafeRepo("releases")

{% if cookiecutter.sbt_scalariform_version != '-' %}
addSbtPlugin("org.scalariform" % "sbt-scalariform" % "{{ cookiecutter.sbt_scalariform_version }}")
{% endif %}
{% if cookiecutter.scoverage_version != '-' %}
addSbtPlugin("org.scoverage" % "sbt-scoverage" % "{{ cookiecutter.scoverage_version }}")
{% endif %}
