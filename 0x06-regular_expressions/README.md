#Regex in Ruby: A Powerful Text Processing Tool
Ruby offers powerful built-in functionality for working with regular expressions (regex). Here's a glimpse into what you can achieve:

##Pattern Matching:

Regex lets you define patterns to search for specific text formats in strings.
For example, you can search for email addresses, phone numbers, or specific words.
'''
text = "This is my email: user@domain.com"
pattern = /\w+@\w+\.\w+/ # Matches email format (word@word.word)
match = text.match(pattern)

if match
  puts "Email found: #{match[0]}"  # Access the matched email
else
  puts "No email found"
end
'''Ruby
