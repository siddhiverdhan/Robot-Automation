*** Settings ***
Documentation       Read the text contained in PDF files and save it to a
...                 corresponding text file.

Library             RPA.PDF
Library             RPA.FileSystem


*** Tasks ***
Extract text from PDF files
    Extract text from PDF file into a text file    simple-text-example.pdf
    Extract text from PDF file into a text file    example-invoice.pdf


*** Keywords ***
Extract text from PDF file into a text file
    [Arguments]    ${pdf_file_name}
    ${text}=    Get Text From Pdf    ${pdf_file_name}
    Create File    ${OUTPUT_DIR}${/}${pdf_file_name}.txt
    FOR    ${page}    IN    @{text.keys()}
        Append To File
        ...    ${OUTPUT_DIR}${/}${pdf_file_name}.txt
        ...    ${text[${page}]}
    END