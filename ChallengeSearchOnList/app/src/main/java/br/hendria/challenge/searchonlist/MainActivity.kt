package br.hendria.challenge.searchonlist

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.widget.ArrayAdapter
import android.widget.EditText
import android.widget.ListView
import java.lang.Integer.min
import kotlin.math.abs

class MainActivity : AppCompatActivity() {

    private val wordList = mutableListOf(
        "medicine", "rich", "blue", "temperature", "fence", "park",
        "simplest", "wrapped", "rough", "old", "discussion", "ranch",
        "branch", "trunk", "breathing", "dangerous", "follow", "matter",
        "average", "heard", "while", "drive", "children", "general", "gulf",
        "threw", "appropriate", "mud", "chest", "hard", "scientist", "count",
        "older", "strong", "six", "very", "source", "get", "primitive", "poetry",
        "figure", "success", "rubbed", "guide", "rose", "jet", "judge", "forward",
        "cell", "suit", "bread", "season", "nice", "cannot", "serve", "shaking",
        "brought", "brother", "left", "silent", "hello", "press", "sitting",
        "seldom", "product", "allow", "yesterday", "across", "has", "great",
        "pick", "away", "married", "pair", "baseball", "widely", "mostly", "tube",
        "amount", "voice", "reason", "characteristic", "fair", "foot",
        "scared", "able", "bad", "friend", "smoke", "large", "garage", "alone",
        "happy", "range", "silk", "zoo", "dry", "ring", "snow", "border"
    )
    private var filteredWords = mutableListOf<String>()

    private lateinit var listAdapter: ArrayAdapter<String>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        filteredWords.addAll(wordList)
        listAdapter = ArrayAdapter(this,  android.R.layout.simple_list_item_1, filteredWords)

        val listView = findViewById<ListView>(R.id.listView)
        listView.adapter = listAdapter


        val searchField = findViewById<EditText>(R.id.searchField)
        searchField.addTextChangedListener(object : TextWatcher{
            override fun afterTextChanged(s: Editable?) {
                // Not used
            }
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
                // Not used
            }
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                Log.d("Challenge", "Text changed: $s")
                val searchTerm = s.toString()

                // If field is empty, clear filters
                if(searchTerm.isBlank()) {
                    listAdapter.clear()
                    filteredWords.addAll(wordList)
                } else {
                    listAdapter.clear()

                    val filteredResults = wordList.filter { word ->
                        // If it is a perfect match
                        if(word == searchTerm) {
                            return@filter true
                        } else {
                            val isPermutation = isPartialPermutation(word, searchTerm)
                            val isTypoWord = isTypo(word, searchTerm)

                            // The user expects that the search returns a result even if word typed is partially
                            // permuted or it has one typo (like explained on previous problems), but not both.
                            return@filter (isPermutation && !isTypoWord) || (!isPermutation && isTypoWord)
                        }
                    }

                    if(filteredResults.isNotEmpty()) {
                        filteredWords.addAll(filteredResults)
                    }
                }


            }

        })
    }


    private fun isPartialPermutation(word: String, term: String): Boolean {
        // Check if the first letter hasn’t changed place
        if(word[0] != term[0]) {
            return false
        }

        val size1 = word.length
        val size2 = term.length

        // Check if word has more than 3 letters
        if(size1 > 3) {
            var sharedLetters = 0

            var smallerLength = min(size1, size2) - 1

            //Count shared letters
            for(i in 0..smallerLength) {
                if(word[i] == term[i]) {
                    sharedLetters += 1
                }
            }
            // Calculate changed letters
            var changedLetters = (size1 - sharedLetters).toFloat()

            //Check is percentage is under 66%
            return changedLetters/size1 < 0.66
        } else {
            return true
        }
    }

    fun getLetterCount(word: String): Map<Char, Int> {
        val letterCount = mutableMapOf<Char, Int>()

        for(letter in word) {
            val mappedValue = letterCount[letter]

            if(mappedValue == null) {
                letterCount[letter] = 1
            } else {
                letterCount[letter] =  mappedValue + 1
            }
        }
        return letterCount
    }

    fun isTypo(word1: String, word2: String): Boolean {
        val letterCount1 = getLetterCount(word1)
        val letterCount2 = getLetterCount(word2)

        val size1 = word1.length
        var matchingLetters = 0

        // Check each letter present on first word
        for(key in letterCount1.keys) {
            // Verify if it is present on the second dictionary
            if(letterCount2.containsKey(key)) {
                // Increment matching letter count
                matchingLetters += 1
            }
        }

        // Calculate the difference in matching letters
        val difference = abs(size1 - matchingLetters)
        return difference <= 1
    }

}
