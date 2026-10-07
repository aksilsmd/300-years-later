*** Settings ***
Documentation     Tests E2E de la landing page (référence ou build React).
...               Exécution : robot --outputdir results -v URL:http://localhost:4173 tests/robot
...               Sans variable URL, la landing de référence est testée depuis le disque.
Library           Browser
Library           String
Suite Setup       New Browser    chromium    headless=True
Suite Teardown    Close Browser

*** Variables ***
${URL}            file://${CURDIR}/../../marketing/landing/index.html

*** Test Cases ***
Le titre et l'appel à l'action sont visibles
    New Page    ${URL}
    Get Title    contains    Afterloom
    Get Element States    css=.hero .btn    contains    visible
    Get Text    css=.hero .btn    ==    Ajouter à ma liste de souhaits

La page passe en anglais
    New Page    ${URL}
    Click    css=.lang button >> text=EN
    Get Text    css=.hero .btn    ==    Add to my wishlist
    Get Attribute    html    lang    ==    en

Le mouvement réduit est respecté
    New Context    reducedMotion=reduce
    New Page    ${URL}
    Sleep    2s
    Get Text    id=year-num    ==    0

Les strates changent l'époque de la page
    New Page    ${URL}
    Sleep    7s
    Scroll To Element    css=.layer[data-era="3"]
    Sleep    1.5s
    ${era}=    Get Attribute    html    data-era
    Should Be Equal    ${era}    3

Aucune ressource externe ni traceur
    New Page    ${URL}
    ${hosts}=    Evaluate JavaScript    ${None}    () => performance.getEntriesByType('resource').map(r => r.name).filter(n => !n.startsWith('file:') && !n.startsWith(location.origin))
    Length Should Be    ${hosts}    0
    ${cookies}=    Get Cookies
    Length Should Be    ${cookies}    0

Le lien d'évitement est accessible au clavier
    New Page    ${URL}
    Keyboard Key    press    Tab
    Get Element States    css=.skip    contains    focused

Les liens légaux existent
    New Page    ${URL}
    Get Element Count    css=.foot nav a    ==    3
