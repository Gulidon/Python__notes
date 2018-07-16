RE使用大致步骤

    使用complic将表示正则的字符串编译未一个pattern对象
    通过pattern对象提供一系列方法对文本进行查找和匹配，获得匹配结果，一个Match对象，最后使用Match对象提供的属性和放大获得信息，根据需要进行操作 #RE常用函数
    group（）：获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，直接使用group或group（0）
    start： 获取分组匹配的子串再整个字符中的真实位置，参数默认为0
    end: 获取分组匹配的子串在整个字符串中的结束位置，默认为0
    span：返回的结构技术（start（group），end（group））

import re

help(re)

Help on module re:

NAME
    re - Support for regular expressions (RE).

DESCRIPTION
    This module provides regular expression matching operations similar to
    those found in Perl.  It supports both 8-bit and Unicode strings; both
    the pattern and the strings being processed can contain null bytes and
    characters outside the US ASCII range.
    
    Regular expressions can contain both special and ordinary characters.
    Most ordinary characters, like "A", "a", or "0", are the simplest
    regular expressions; they simply match themselves.  You can
    concatenate ordinary characters, so last matches the string 'last'.
    
    The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        *?,+?,?? Non-greedy versions of the previous three special characters.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Non-greedy version of the above.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.
                 The contents can be retrieved or matched later in the string.
        (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
        (?:...)  Non-grouping version of regular parentheses.
        (?P<name>...) The substring matched by the group is accessible by name.
        (?P=name)     Matches the text matched earlier by the group named name.
        (?#...)  A comment; ignored.
        (?=...)  Matches if ... matches next, but doesn't consume the string.
        (?!...)  Matches if ... doesn't match next.
        (?<=...) Matches if preceded by ... (must be fixed length).
        (?<!...) Matches if not preceded by ... (must be fixed length).
        (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                           the (optional) no pattern otherwise.
    
    The special sequences consist of "\\" and a character from the list
    below.  If the ordinary character is not on the list, then the
    resulting RE will match the second character.
        \number  Matches the contents of the group of the same number.
        \A       Matches only at the start of the string.
        \Z       Matches only at the end of the string.
        \b       Matches the empty string, but only at the start or end of a word.
        \B       Matches the empty string, but not at the start or end of a word.
        \d       Matches any decimal digit; equivalent to the set [0-9] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode digits.
        \D       Matches any non-digit character; equivalent to [^\d].
        \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode whitespace characters.
        \S       Matches any non-whitespace character; equivalent to [^\s].
        \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
                 in bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the
                 range of Unicode alphanumeric characters (letters plus digits
                 plus underscore).
                 With LOCALE, it will match the set [0-9_] plus characters defined
                 as letters for the current locale.
        \W       Matches the complement of \w.
        \\       Matches a literal backslash.
    
    This module exports the following functions:
        match     Match a regular expression pattern to the beginning of a string.
        fullmatch Match a regular expression pattern to all of a string.
        search    Search a string for the presence of a pattern.
        sub       Substitute occurrences of a pattern found in a string.
        subn      Same as sub, but also return the number of substitutions made.
        split     Split a string by the occurrences of a pattern.
        findall   Find all occurrences of a pattern in a string.
        finditer  Return an iterator yielding a match object for each match.
        compile   Compile a pattern into a RegexObject.
        purge     Clear the regular expression cache.
        escape    Backslash all non-alphanumerics in a string.
    
    Some of the functions in this module takes flags as optional parameters:
        A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                       match the corresponding ASCII character categories
                       (rather than the whole Unicode categories, which is the
                       default).
                       For bytes patterns, this flag is the only available
                       behaviour and needn't be specified.
        I  IGNORECASE  Perform case-insensitive matching.
        L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
        M  MULTILINE   "^" matches the beginning of lines (after a newline)
                       as well as the string.
                       "$" matches the end of lines (before a newline) as well
                       as the end of the string.
        S  DOTALL      "." matches any character at all, including the newline.
        X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
        U  UNICODE     For compatibility only. Ignored for string patterns (it
                       is the default), and forbidden for bytes patterns.
    
    This module also defines an exception 'error'.

CLASSES
    builtins.Exception(builtins.BaseException)
        sre_constants.error
    
    class error(builtins.Exception)
     |  Exception raised for invalid regular expressions.
     |  
     |  Attributes:
     |  
     |      msg: The unformatted error message
     |      pattern: The regular expression pattern
     |      pos: The index in the pattern where compilation failed (may be None)
     |      lineno: The line corresponding to pos (may be None)
     |      colno: The column corresponding to pos (may be None)
     |  
     |  Method resolution order:
     |      error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, msg, pattern=None, pos=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    compile(pattern, flags=0)
        Compile a regular expression pattern, returning a pattern object.
    
    escape(pattern)
        Escape all the characters in pattern except ASCII letters, numbers and '_'.
    
    findall(pattern, string, flags=0)
        Return a list of all non-overlapping matches in the string.
        
        If one or more capturing groups are present in the pattern, return
        a list of groups; this will be a list of tuples if the pattern
        has more than one group.
        
        Empty matches are included in the result.
    
    finditer(pattern, string, flags=0)
        Return an iterator over all non-overlapping matches in the
        string.  For each match, the iterator returns a match object.
        
        Empty matches are included in the result.
    
    fullmatch(pattern, string, flags=0)
        Try to apply the pattern to all of the string, returning
        a match object, or None if no match was found.
    
    match(pattern, string, flags=0)
        Try to apply the pattern at the start of the string, returning
        a match object, or None if no match was found.
    
    purge()
        Clear the regular expression caches
    
    search(pattern, string, flags=0)
        Scan through string looking for a match to the pattern, returning
        a match object, or None if no match was found.
    
    split(pattern, string, maxsplit=0, flags=0)
        Split the source string by the occurrences of the pattern,
        returning a list containing the resulting substrings.  If
        capturing parentheses are used in pattern, then the text of all
        groups in the pattern are also returned as part of the resulting
        list.  If maxsplit is nonzero, at most maxsplit splits occur,
        and the remainder of the string is returned as the final element
        of the list.
    
    sub(pattern, repl, string, count=0, flags=0)
        Return the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in string by the
        replacement repl.  repl can be either a string or a callable;
        if a string, backslash escapes in it are processed.  If it is
        a callable, it's passed the match object and must return
        a replacement string to be used.
    
    subn(pattern, repl, string, count=0, flags=0)
        Return a 2-tuple containing (new_string, number).
        new_string is the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in the source
        string by the replacement repl.  number is the number of
        substitutions that were made. repl can be either a string or a
        callable; if a string, backslash escapes in it are processed.
        If it is a callable, it's passed the match object and must
        return a replacement string to be used.
    
    template(pattern, flags=0)
        Compile a template pattern, returning a pattern object

DATA
    A = <RegexFlag.ASCII: 256>
    ASCII = <RegexFlag.ASCII: 256>
    DOTALL = <RegexFlag.DOTALL: 16>
    I = <RegexFlag.IGNORECASE: 2>
    IGNORECASE = <RegexFlag.IGNORECASE: 2>
    L = <RegexFlag.LOCALE: 4>
    LOCALE = <RegexFlag.LOCALE: 4>
    M = <RegexFlag.MULTILINE: 8>
    MULTILINE = <RegexFlag.MULTILINE: 8>
    S = <RegexFlag.DOTALL: 16>
    U = <RegexFlag.UNICODE: 32>
    UNICODE = <RegexFlag.UNICODE: 32>
    VERBOSE = <RegexFlag.VERBOSE: 64>
    X = <RegexFlag.VERBOSE: 64>
    __all__ = ['match', 'fullmatch', 'search', 'sub', 'subn', 'split', 'fi...

VERSION
    2.2.1

FILE
    d:\programdata\anaconda3\lib\re.py


#导入相关包

import re

#查找数字

# r表示字符串不转义

p = re.compile(r'\d+')

#在字符串“one12twothree33456four78”中进行查找，按照规则p制定的正则进行查找

#参数3,6表示字符串中的查找范围

m = p.match("one12twothree33456four78", 3, 26)

​

print(m)

​

#match可以输入参数表示起始位置

#match查找结果只有一个，即第一次匹配成功的内容

<_sre.SRE_Match object; span=(3, 5), match='12'>

print(m[0])

print(m.start())#起始

print(m.end())#结束

12
3
5

import re

​

p = re.compile(r'([a-z]+) ([a-z]+)', re.I)#([a-z]+)之间有空格   I表示忽略大小写

​

m = p.match("I am really love wangxiaojing")

print(m)

<_sre.SRE_Match object; span=(0, 4), match='I am'>

print(m.group(0))

print(m.start())#起始

print(m.end())#结束

I am
0
4

print(m.group(1))

print(m.start(1))

print(m.end(1))

I
0
1

查找

    search（str，[,pos[, endpos]]）：在字符串中查找匹配，pos和endpos表示起始位置
    findall： 查找所有
    finditer： 查找，返回一个iter结果

import re

p = re.compile(r'\d+')

​

m = p.search("one12twothree33456four78")

​

print(m.group())

12

rst = p.findall("one12twothree33456four78")

print(type(rst))

print(rst)

<class 'list'>
['12', '33456', '78']

sub 替换

    sub（rep1， str[, count]）

import re

p = re.compile(r'(\w+) (\w+)')

s = "hello 123 wang 456 xiaojing, i love you"

rst = p.sub(r'Hello world', s)

print(rst)

Hello world Hello world xiaojing, Hello world you

匹配中文

    大部分中文内容表示范围是[u4e00-u9fa5]，不包括全角标点

import re

title = u'世界 你好， hello moto'

p = re.compile(r'[\u4e00-\u9fa5]+')

rst = p.findall(title)

print(rst)

['世界', '你好']

贪婪和非贪婪

    贪婪：尽可能多的匹配，（*）表示贪婪匹配
    非贪婪：找到符合条件的最小内容即可，（？）表示非贪婪
    正则默认使用贪婪匹配

import re

title = u'<div>name</div><div>age</div>'

p1 = re.compile(r"<div>.*</div>")

p2 = re.compile(r"<div>.*?</div>")

​

m1 = p1.search(title)

print(m1.group())

​

m2 = p2.search(title)

print(m2.group())

<div>name</div><div>age</div>
<div>name</div>
