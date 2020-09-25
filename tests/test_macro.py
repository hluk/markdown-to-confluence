def test_macro_jiraissues(script):
    """
    Test jiraissues macro for listing Jira issues.

    Format:

        [jira:param1=value1;pram2=value2)](OPTIONAL_LINK)
    """
    script.set_content(
        "[jira:jqlQuery=filter=666 ORDER BY updated DESC;columns=a,b,c]"
        "(ignored_link_when_converted)"
    )
    assert (
        "<p>"
        '<ac:structured-macro ac:name="jiraissues">'
        '<ac:parameter ac:name="jqlQuery">filter=666 ORDER BY updated DESC</ac:parameter>'
        '<ac:parameter ac:name="columns">a,b,c</ac:parameter>'
        "</ac:structured-macro>"
        "</p>"
    ) in script.run()


def test_html_macro(script):
    """
    Test that we can use raw HTML enclosed in div elements.
    """
    script.set_content(
        '<div>'
        '<ac:structured-macro ac:name="jiraissues">'
        '<ac:parameter ac:name="filter">666</ac:parameter>'
        '<ac:parameter ac:name="columns">a,b,c</ac:parameter>'
        "</ac:structured-macro>"
        '</div>'
    )
    assert (
        "<div>"
        '<ac:structured-macro ac:name="jiraissues">'
        '<ac:parameter ac:name="filter">666</ac:parameter>'
        '<ac:parameter ac:name="columns">a,b,c</ac:parameter>'
        "</ac:structured-macro>"
        "</div>"
    ) in script.run()
