// 1. an almost complete python grammar in simple JSON format
var http_config_grammarDefinition = {
    
    // prefix ID for regular expressions used in the grammar
    "RegExpID" : "RegExp::",

    //
    // Style model
    "Style" : {
        // lang token type  -> Editor (style) tag
        "decorator":    "constant.support",
        "comment":      "comment",
        "keyword":      "keyword",
        "builtin":      "constant.support",
        "variable":     "variable",
        "operator":     "constant",
        "identifier":   "identifier",
        "number":       "constant.numeric",
        "heredoc":      "string",
        "ViewService":  "string.regexp",
        "TstServer":    "string.regexp" ,
        "TstService" :  "string.regexp"
    },
    
    //
    // Lexical model
    "Lex" : {
    
        // comments
        "comment" : {
            "type" : "comment",
            "tokens" : [
                // null delimiter, matches end-of-line
                ["#",  null],
                ["/*",  "*/"]
            ]
        },
               
        // View External Service
        "ViewService" : [ 
                       "RegExp::/\\<(.*?\>)\>*/"
                    ],

        // test sub service
        "TstService" : [ 
                       "RegExp::/\\[\\[(.*\\]?)\\]\\]*/"
                    ],              

        "TstServer" : [ 
                       "RegExp::/\\[(.*\\]?)\\]*/"
                    ],              
                            
        
        // php variables
        "variable" :  [ 
                       "RegExp::/\\$\\{(.*?\\})\\}*/",
                       "RegExp::/\\|[_A-Za-z][_A-Za-z0-9]*/",
                       "RegExp::/\\![_A-Za-z][_A-Za-z0-9]*/"
                      ],

        
        // blocks, in this case heredocs
        "heredoc" : {
            "type" : "escaped-block",
            "escape" : "\\",
            "tokens" : [ 
                // begin and end of heredocs
                // if no end given, end is same as start of block                
                [ "RegExp::/\"\"\"/",], // """ string \" pattern"""
                [ "RegExp::/\'\'\'/",], // ''' string \' pattern'''
                [ "RegExp::/\"/",],     // ' string \' pattern'
                [ "RegExp::/\'/",],     // " string \" pattern"
                ["||"],    // config obfuscated password colour
                [ "RegExp::/([rubRUB]|(ur)|(br)|(UR)|(BR))?('{3}|\"{3})/", 6 ] 
            ]
        },
        
        // general identifiers
        "identifier" : "RegExp::/[_A-Za-z][_A-Za-z0-9]*/",

        // numbers, in order of matching
        "number" : [
            // floats
            "RegExp::/\\d*\\.\\d+(e[\\+\\-]?\\d+)?[jJ]?/",
            "RegExp::/\\d+\\.\\d*[jJ]?/",
            "RegExp::/\\.\\d+[jJ]?/",
            // integers
            // hex
            "RegExp::/0x[0-9a-fA-F]+[lL]?/",
            // binary
            "RegExp::/0b[01]+[lL]?/",
            // octal
            "RegExp::/0o[0-7]+[lL]?/",
            // decimal
            "RegExp::/[1-9]\\d*(e[\\+\\-]?\\d+)?[lL]?[jJ]?/",
            // just zero
            "RegExp::/0(?![\\dx])/"
        ],

        // strings
        "string" : {
            "type" : "escaped-block",
            "escape" : "",
            "tokens" : [ 
                // start, end of string (can be the matched regex group ie. 1 )
                [ "RegExp::/(['\"])/", 1 ], 
                [ "RegExp::/([rubRUB]|(ur)|(br)|(UR)|(BR))?(['\"])/", 6 ] 
            ]
        },
        
        // operators
        "operator" : {
            "combine" : true,
            "tokens" : [
                "*", "=", "+", "-", "==", ":" 
            ]
        },
        
        // delimiters
        "delimiter" : {
            "combine" : true,
            "tokens" : [ 
                "(", ")", "[", "]", "<", ">", "${", "}"
            ]
        },

        // decorators
        "decorator" : "RegExp::/@[_A-Za-z][_A-Za-z0-9]*/",

        // keywords
        "keyword" : {
            // enable autocompletion for these tokens, with their associated token ID
            "autocomplete" : true,
            "tokens" : [
                "RegExp::/INCLUDE/i",
                "RegExp::/END-SCOPE-GLOBAL/i",
                "RegExp::/END-SCOPE/i"
            ]
        },
                              
        // builtin functions, constructs, etc..
        "builtin" : {
            // enable autocompletion for these tokens, with their associated token ID
            "autocomplete" : true,
            "tokens" : [""
            ]
        }
    },

    //
    // Syntax model (optional)
    //"Syntax" : null,
    
    // what to parse and in what order
    "Parser" : [
        "variable",
        "heredoc",
        "comment", 
        "ViewService", 
        "TstService",              
        "TstServer",  
        "number",
        "decorator",
        "operator",
        "delimiter",
        "keyword",
        "builtin",
        "identifier",       
    ]
};
