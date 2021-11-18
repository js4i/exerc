from validator import valida_cdvpy


class TestValidation():

    def test_valida_cdvpy__test_with_valid_cdvpy__expected_True(
        self
    ):
        # FIXTURE
        cdvpy = '123456'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == True

    def test_valida_cdvpy__test_with_more_than_six_digits__expected_False(
        self
    ):
        # FIXTURE
        cdvpy = '1234567'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == False

    def test_valida_cdvpy__test_with_less_than_six_digits__expected_False(
        self
    ):
        # FIXTURE
        cdvpy = '12345'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == False

    def test_valida_cdvpy__test_with_letter_and_digits__expected_False(
        self
    ):
        # FIXTURE
        cdvpy = 'A12345'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == False

    def test_valida_cdvpy__test_with_zero_at_the_beginning__expected_False(
        self
    ):
        # FIXTURE
        cdvpy = '012345'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == False

    def test_valida_cdvpy__test_with_zero_at_the_end__expected_True(
        self
    ):
        # FIXTURE
        cdvpy = '512340'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == True

    def test_valida_cdvpy__test_with_repeated_digits_pair__expected_False(
        self
    ):
        # FIXTURE
        cdvpy = '552523'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == False

    def test_valida_cdvpy__test_with_one_repeated_digits__expected_True(
        self
    ):
        # FIXTURE
        cdvpy = '123451'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == True

    def test_valida_cdvpy__test_with_many_repeated_digits__expected_True(
        self
    ):
        # FIXTURE
        cdvpy = '121323'

        # EXERCISE
        result = valida_cdvpy(cdvpy)

        # ASSERTS
        assert result == True
