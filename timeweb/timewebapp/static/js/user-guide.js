document.addEventListener("DOMContentLoaded", function() {
    const LABEL_ICON_TEMPLATE = $("#label-icon-template").html();
    $(".label-question").each(function() {
        $(this).append($(LABEL_ICON_TEMPLATE));
    });
    const TABLE_OF_CONTENTS_MAJOR_CATEGORY_TEMPLATE = $("#table-of-contents-major-category-template").html();
    const TABLE_OF_CONTENTS_MINOR_CATEGORY_TEMPLATE = $("#table-of-contents-minor-category-template").html();

    const number_major_categories = $(".major-category").length;
    $(".major-category").reverse().each(function() {
        const $major_category = $(this);
        $major_category.attr("number-major-categories", number_major_categories);

        const major_category_li = $(TABLE_OF_CONTENTS_MAJOR_CATEGORY_TEMPLATE);
        major_category_li.find("a").text($major_category.text());
        $major_category.attr("id") && major_category_li.find("a").attr("href", `#${$major_category.attr("id")}`);

        $major_category.siblings("details").each(function() {
            const $minor_category = $(this).find(".minor-category");

            const minor_category_li = $(TABLE_OF_CONTENTS_MINOR_CATEGORY_TEMPLATE);
            minor_category_li.find("a").attr("href", `#${$minor_category.attr("id")}`).text($minor_category.text());
            major_category_li.find("ul").append(minor_category_li);
        });
        $("#table-of-contents-container #category-table-of-contents").after(major_category_li);
    });

    $(".label-question").each(function() {
        const $label_question = $(this);

        const minor_category_li = $(TABLE_OF_CONTENTS_MINOR_CATEGORY_TEMPLATE);
        minor_category_li.find("a").attr("href", `#${$label_question.attr("id")}`).text($label_question.find(".label-title").text());

        $("#table-of-contents-container #category-user-guide-labels").append(minor_category_li);
    });
});