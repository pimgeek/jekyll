# module Jekyll
#   class URL
#     def self.escape_path(path)
#       # Because URI.escape doesn't escape '?', '[' and ']' by default,
#       # specify unsafe string (except unreserved, sub-delims, ":", "@" and "/").
#       #
#       # URI path segment is defined in RFC 3986 as follows:
#       #   segment       = *pchar
#       #   pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"
#       #   unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
#       #   pct-encoded   = "%" HEXDIG HEXDIG
#       #   sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
#       #                 / "*" / "+" / "," / ";" / "="
#       # URI.escape(path, /[^a-zA-Z\d\-._~!$&\'()*+,;=:@\/]/).encode('utf-8')
#       path
#     end
#   end
# end