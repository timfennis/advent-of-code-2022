package day1

import java.io.File

fun main() {
    val text = File("./src/main/kotlin/day1/input").readText()
    val data = text.split("\n\n")
        .map { group ->
            group.split("\n")
                .sumOf { line -> line.toInt() }
        }
        .sorted()
        .reversed()

    println("First: ${data.first()}")
    println("Second: ${data.slice(0..2).sum()}")
}