object CollatzCalculator {
    fun computeStepCount(start: Int): Int {
        require(start > 0) { "Only positive integers are allowed" }
        var count = 0
        var number = start

        while (number != 1) {
            number = if (number % 2 == 0) {
                number / 2
            } else {
                3 * number + 1
            }
            count++
        }

        return count
    }
    }
