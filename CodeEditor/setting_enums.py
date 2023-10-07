"""Wrapper for Qsci.QsciScintilla enumerations.
"""
from PyQt6.Qsci import QsciScintilla
from PyQt6.QtCore import QCoreApplication, Qt
from CodeEditor.lang import language_extensions


class EnumError(Exception):
    """unknown enum name or get enum failed."""
    def __init__(self, name):
        super(EnumError, self).__init__("Unknown enumeration: {}".format(name))


class SettingEnums:
    enums = {
        # annotation display styles
        QsciScintilla.AnnotationDisplay: {
            QsciScintilla.AnnotationDisplay.AnnotationHidden: {
                'name': 'AnnotationHidden',
                'display': QCoreApplication.translate('SettingEnums', "Hidden")
            },
            QsciScintilla.AnnotationDisplay.AnnotationStandard: {
                'name': 'AnnotationStandard',
                'display': QCoreApplication.translate('SettingEnums', "Standard")
            },
            QsciScintilla.AnnotationDisplay.AnnotationBoxed: {
                'name': 'AnnotationBoxed',
                'display': QCoreApplication.translate('SettingEnums', "Boxed")
            },
        },
        # sources for auto-completion lists.
        QsciScintilla.AutoCompletionSource: {
            QsciScintilla.AutoCompletionSource.AcsNone: {
                'name': 'AcsNone',
                'display': QCoreApplication.translate('SettingEnums', "None")
            },
            QsciScintilla.AutoCompletionSource.AcsAll: {
                'name': 'AcsAll',
                'display': QCoreApplication.translate('SettingEnums', "All")
            },
            QsciScintilla.AutoCompletionSource.AcsDocument: {
                'name': 'AcsDocument',
                'display': QCoreApplication.translate('SettingEnums', "Document")
            },
            QsciScintilla.AutoCompletionSource.AcsAPIs: {
                'name': 'AcsAPIs',
                'display': QCoreApplication.translate('SettingEnums', "APIs")
            },
        },
        # brace matching modes. The character pairs (), [] and () are treated as
        # braces. The Python lexers will also match a : with the end of the
        # corresponding indented block.
        QsciScintilla.BraceMatch: {
            QsciScintilla.BraceMatch.NoBraceMatch: {
                'name': 'NoBraceMatch',
                'display': QCoreApplication.translate('SettingEnums', "No")
            },
            QsciScintilla.BraceMatch.StrictBraceMatch: {
                'name': 'StrictBraceMatch',
                'display': QCoreApplication.translate('SettingEnums', "Strict")
            },
            QsciScintilla.BraceMatch.SloppyBraceMatch: {
                'name': 'SloppyBraceMatch',
                'display': QCoreApplication.translate('SettingEnums', "Sloppy")
            },
        },
        # call tip styles
        QsciScintilla.CallTipsStyle: {
            QsciScintilla.CallTipsStyle.CallTipsNone: {
                'name': 'CallTipsNone',
                'display': QCoreApplication.translate('SettingEnums', "None")
            },
            QsciScintilla.CallTipsStyle.CallTipsNoContext: {
                'name': 'CallTipsNoContext',
                'display': QCoreApplication.translate('SettingEnums', "NoContext")
            },
            QsciScintilla.CallTipsStyle.CallTipsNoAutoCompletionContext: {
                'name': 'CallTipsNoAutoCompletionContext',
                'display': QCoreApplication.translate('SettingEnums', "NoAutoCompletionContext")
            },
            QsciScintilla.CallTipsStyle.CallTipsContext: {
                'name': 'CallTipsContext',
                'display': QCoreApplication.translate('SettingEnums', "Context")
            },
        },
        # edge modes for long lines
        QsciScintilla.EdgeMode: {
            QsciScintilla.EdgeMode.EdgeNone: {
                'name': 'EdgeNone',
                'display': 'None'
            },
            QsciScintilla.EdgeMode.EdgeLine: {
                'name': 'EdgeLine',
                'display': 'Line'
            },
            QsciScintilla.EdgeMode.EdgeBackground: {
                'name': 'EdgeBackground',
                'display': 'Background'
            }
        },
        # end-of-line modes
        QsciScintilla.EolMode: {
            QsciScintilla.EolMode.EolWindows: {
                'name': 'EolWindows',
                'display': 'Windows'
            },
            QsciScintilla.EolMode.EolUnix: {
                'name': 'Unix',
                'display': 'Unix'
            },
            QsciScintilla.EolMode.EolMac: {
                'name': 'EolMac',
                'display': 'Mac'
            }
        },
        # styles for the folding margin
        QsciScintilla.FoldStyle: {
            QsciScintilla.FoldStyle.NoFoldStyle: {
                'name': 'NoFoldStyle',
                'display': 'No'
            },
            QsciScintilla.FoldStyle.PlainFoldStyle: {
                'name': 'PlainFoldStyle',
                'display': 'Plain'
            },
            QsciScintilla.FoldStyle.CircledFoldStyle: {
                'name': 'CircledFoldStyle',
                'display': 'Circled'
            },
            QsciScintilla.FoldStyle.BoxedFoldStyle: {
                'name': 'BoxedFoldStyle',
                'display': 'Boxed'
            },
            QsciScintilla.FoldStyle.CircledTreeFoldStyle: {
                'name': 'CircledTreeFoldStyle',
                'display': 'CircledTree'
            },
            QsciScintilla.FoldStyle.BoxedTreeFoldStyle: {
                'name': 'BoxedTreeFoldStyle',
                'display': 'BoxedTree'
            }
        },
        # margin types
        QsciScintilla.MarginType: {
            QsciScintilla.MarginType.SymbolMargin: {
                'name': 'NoFoldStyle',
                'display': 'NoFoldStyle'
            },
            QsciScintilla.MarginType.SymbolMarginDefaultForegroundColor: {
                'name': 'PlainFoldStyle',
                'display': 'PlainFoldStyle'
            },
            QsciScintilla.MarginType.SymbolMarginDefaultBackgroundColor: {
                'name': 'CircledFoldStyle',
                'display': 'CircledFoldStyle'
            },
            QsciScintilla.MarginType.NumberMargin: {
                'name': 'BoxedFoldStyle',
                'display': 'BoxedFoldStyle'
            },
            QsciScintilla.MarginType.TextMargin: {
                'name': 'CircledTreeFoldStyle',
                'display': 'CircledTreeFoldStyle'
            },
            QsciScintilla.MarginType.TextMarginRightJustified: {
                'name': 'BoxedTreeFoldStyle',
                'display': 'BoxedTreeFoldStyle'
            }
        },
        # pre-defined marker symbols   #25 28 tobe added
        QsciScintilla.MarkerSymbol: {
            QsciScintilla.MarkerSymbol.Circle: {
                'name': 'Circle',
                'display': 'Circle'
            },
            QsciScintilla.MarkerSymbol.Rectangle: {
                'name': 'Rectangle',
                'display': 'Rectangle'
            },
            QsciScintilla.MarkerSymbol.RightTriangle: {
                'name': 'RightTriangle',
                'display': 'RightTriangle'
            },
            QsciScintilla.MarkerSymbol.SmallRectangle: {
                'name': 'SmallRectangle',
                'display': 'SmallRectangle'
            },
            QsciScintilla.MarkerSymbol.RightArrow: {
                'name': 'RightArrow',
                'display': 'RightArrow'
            },
            QsciScintilla.MarkerSymbol.Invisible: {
                'name': 'Invisible',
                'display': 'Invisible'
            },
            QsciScintilla.MarkerSymbol.DownTriangle: {
                'name': 'DownTriangle',
                'display': 'DownTriangle'
            },
            QsciScintilla.MarkerSymbol.Minus: {
                'name': 'Minus',
                'display': 'Minus'
            },
            QsciScintilla.MarkerSymbol.Plus: {
                'name': 'Plus',
                'display': 'Plus'
            },
            QsciScintilla.MarkerSymbol.VerticalLine: {
                'name': 'VerticalLine',
                'display': 'VerticalLine'
            },
            QsciScintilla.MarkerSymbol.BottomLeftCorner: {
                'name': 'BottomLeftCorner',
                'display': 'BottomLeftCorner'
            },
            QsciScintilla.MarkerSymbol.LeftSideSplitter: {
                'name': 'LeftSideSplitter',
                'display': 'LeftSideSplitter'
            },
            QsciScintilla.MarkerSymbol.BoxedPlus: {
                'name': 'BoxedPlus',
                'display': 'BoxedPlus'
            },
            QsciScintilla.MarkerSymbol.BoxedPlusConnected: {
                'name': 'BoxedPlusConnected',
                'display': 'BoxedPlusConnected'
            },
            QsciScintilla.MarkerSymbol.BoxedMinus: {
                'name': 'BoxedMinus',
                'display': 'BoxedMinus'
            },
            QsciScintilla.MarkerSymbol.BoxedMinusConnected: {
                'name': 'BoxedMinusConnected',
                'display': 'BoxedMinusConnected'
            },
            QsciScintilla.MarkerSymbol.RoundedBottomLeftCorner: {
                'name': 'RoundedBottomLeftCorner',
                'display': 'RoundedBottomLeftCorner'
            },
            QsciScintilla.MarkerSymbol.LeftSideRoundedSplitter: {
                'name': 'LeftSideRoundedSplitter',
                'display': 'LeftSideRoundedSplitter'
            },
            QsciScintilla.MarkerSymbol.CircledPlus: {
                'name': 'CircledPlus',
                'display': 'CircledPlus'
            },
            QsciScintilla.MarkerSymbol.CircledPlusConnected: {
                'name': 'CircledPlusConnected',
                'display': 'CircledPlusConnected'
            },
            QsciScintilla.MarkerSymbol.CircledMinus: {
                'name': 'CircledMinus',
                'display': 'CircledMinus'
            },
            QsciScintilla.MarkerSymbol.CircledMinusConnected: {
                'name': 'CircledMinusConnected',
                'display': 'CircledMinusConnected'
            },
            QsciScintilla.MarkerSymbol.Background: {
                'name': 'Background',
                'display': 'Background'
            },
            QsciScintilla.MarkerSymbol.ThreeDots: {
                'name': 'ThreeDots',
                'display': 'ThreeDots'
            },
            QsciScintilla.MarkerSymbol.ThreeRightArrows: {
                'name': 'ThreeRightArrows',
                'display': 'ThreeRightArrows'
            },
            QsciScintilla.MarkerSymbol.FullRectangle: {
                'name': 'FullRectangle',
                'display': 'FullRectangle'
            },
            QsciScintilla.MarkerSymbol.LeftRectangle: {
                'name': 'LeftRectangle',
                'display': 'LeftRectangle'
            },
            QsciScintilla.MarkerSymbol.Underline: {
                'name': 'Underline',
                'display': 'Underline'
            }
        },
        # whitespace visibility modes. When whitespace is visible spaces are
        # displayed as small centred dots and tabs are displayed as light arrows
        # pointing to the right.
        QsciScintilla.WhitespaceVisibility: {
            QsciScintilla.WhitespaceVisibility.WsInvisible: {
                'name': 'WsInvisible',
                'display': 'Invisible'
            },
            QsciScintilla.WhitespaceVisibility.WsVisible: {
                'name': 'WsVisible',
                'display': 'Visible'
            },
            QsciScintilla.WhitespaceVisibility.WsVisibleAfterIndent: {
                'name': 'WsVisibleAfterIndent',
                'display': 'VisibleAfterIndent'
            }
        },
        # line wrap modes
        QsciScintilla.WrapMode: {
            QsciScintilla.WrapMode.WrapNone: {
                'name': 'WrapNone',
                'display': 'None'
            },
            QsciScintilla.WrapMode.WrapWord: {
                'name': 'WrapWord',
                'display': 'Word'
            },
            QsciScintilla.WrapMode.WrapCharacter: {
                'name': 'WrapCharacter',
                'display': 'Character'
            }
        },
        # line wrap visual flags
        QsciScintilla.WrapVisualFlag: {
            QsciScintilla.WrapVisualFlag.WrapFlagNone: {
                'name': 'WrapFlagNone',
                'display': 'None'
            },
            QsciScintilla.WrapVisualFlag.WrapFlagByText: {
                'name': 'WrapFlagByText',
                'display': 'ByText'
            },
            QsciScintilla.WrapVisualFlag.WrapFlagByBorder: {
                'name': 'WrapFlagByBorder',
                'display': 'ByBorder'
            }
        },
        # custom list for language
        'language': dict([(lang, {
            'name': lang,
            'display': lang
        }) for (lang, ext) in language_extensions]),
    }
    lookup = dict([(enumtype, dict([(enuminfo['name'], enumvalue) for (enumvalue, enuminfo) in enumvalues.items()]))
                   for (enumtype, enumvalues) in enums.items()])

    @classmethod
    def getName(cls, enumType, enumValue):
        """Return the string version of the enumeration type,
        or raise `BadEnum` if there's no such enumeration type.
        """
        # Invalid enum type or value
        if enumType not in cls.enums:
            raise EnumError(enumType)
        if enumValue not in cls.enums[enumType]:
            raise EnumError(enumValue)
        return cls.enums[enumType][enumValue]['name']

    @classmethod
    def getDisplayString(cls, enumType, enumValue):
        """Return the string display on ui for the enumeration type,
        or raise `BadEnum` if there's no such enumeration type.
        """
        # Invalid enum type or value
        if enumType not in cls.enums:
            raise EnumError(enumType)
        if enumValue not in cls.enums[enumType]:
            raise EnumError(enumValue)
        return cls.enums[enumType][enumValue]['display']

    @classmethod
    def getFromName(cls, enumType, enumName):
        """Return the Qsci.QsciScintilla enum value for the given enume Name."""
        # Invalid enum type or value
        if enumType not in cls.lookup:
            raise EnumError(enumType)
        if enumName not in cls.lookup[enumType]:
            raise EnumError(enumName)
        return cls.lookup[enumType][enumName]
