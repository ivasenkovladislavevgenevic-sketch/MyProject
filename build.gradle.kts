plugins {
    id("java")
    id("net.neoforged.gradle.userdev") version "7.0.171"
}

val modId: String by project
val modVersion: String by project
val modGroupId: String by project
val minecraftVersion: String by project
val neoforgeVersion: String by project

version = modVersion
group = modGroupId

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

minecraft {
    accessTransformers {
        file("src/main/resources/META-INF/accesstransformer.cfg")
    }
}

runs {
    configureEach {
        systemProperty("forge.logging.markers", "REGISTRIES")
        systemProperty("forge.logging.console.level", "debug")
        modSource(project.sourceSets.main.get())
    }

    create("client") {
        systemProperty("forge.enabledGameTestNamespaces", modId)
    }

    create("server") {
        systemProperty("forge.enabledGameTestNamespaces", modId)
        programArgument("--nogui")
    }
}

dependencies {
    implementation("net.neoforged:neoforge:$neoforgeVersion")
}

tasks.withType<ProcessResources>().configureEach {
    val replaceProperties = mapOf(
        "minecraft_version" to minecraftVersion,
        "neoforge_version" to neoforgeVersion,
        "mod_id" to modId,
        "mod_version" to modVersion,
        "mod_name" to project.properties["mod_name"],
        "mod_authors" to project.properties["mod_authors"],
        "mod_description" to project.properties["mod_description"]
    )
    inputs.properties(replaceProperties)
    filesMatching(listOf("META-INF/neoforge.mods.toml")) {
        expand(replaceProperties)
    }
}

tasks.withType<JavaCompile>().configureEach {
    options.encoding = "UTF-8"
}
