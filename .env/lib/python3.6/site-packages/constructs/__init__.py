"""
# Constructs Programming Model

> Define composable configuration models through code

![Release](https://github.com/awslabs/cdk8s/workflows/Release/badge.svg)
[![npm version](https://badge.fury.io/js/constructs.svg)](https://badge.fury.io/js/cdk8s)
[![PyPI version](https://badge.fury.io/py/constructs.svg)](https://badge.fury.io/py/cdk8s)
[![NuGet version](https://badge.fury.io/nu/Constructs.svg)](https://badge.fury.io/nu/Org.Cdk8s)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/software.constructs/constructs/badge.svg?style=plastic)](https://maven-badges.herokuapp.com/maven-central/software.constructs/constructs)

## Contributing

This project has adopted the [Amazon Open Source Code of
Conduct](https://aws.github.io/code-of-conduct).

We welcome community contributions and pull requests. See our [contribution
guide](./CONTRIBUTING.md) for more information on how to report issues, set up a
development environment and submit code.

## License

This project is distributed under the [Apache License, Version 2.0](./LICENSE).
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

__jsii_assembly__ = jsii.JSIIAssembly.load("constructs", "2.0.1", __name__, "constructs@2.0.1.jsii.tgz")


class ConstructMetadata(metaclass=jsii.JSIIMeta, jsii_type="constructs.ConstructMetadata"):
    """Metadata keys used by constructs."""
    @jsii.python.classproperty
    @jsii.member(jsii_name="DISABLE_STACK_TRACE_IN_METADATA")
    def DISABLE_STACK_TRACE_IN_METADATA(cls) -> str:
        """If set in the construct's context, omits stack traces from metadata entries."""
        return jsii.sget(cls, "DISABLE_STACK_TRACE_IN_METADATA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ERROR_METADATA_KEY")
    def ERROR_METADATA_KEY(cls) -> str:
        """Context type for error level messages."""
        return jsii.sget(cls, "ERROR_METADATA_KEY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="INFO_METADATA_KEY")
    def INFO_METADATA_KEY(cls) -> str:
        """Context type for info level messages."""
        return jsii.sget(cls, "INFO_METADATA_KEY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WARNING_METADATA_KEY")
    def WARNING_METADATA_KEY(cls) -> str:
        """Context type for warning level messages."""
        return jsii.sget(cls, "WARNING_METADATA_KEY")


@jsii.data_type(jsii_type="constructs.ConstructOptions", jsii_struct_bases=[], name_mapping={'node_factory': 'nodeFactory'})
class ConstructOptions():
    def __init__(self, *, node_factory: typing.Optional["INodeFactory"]=None):
        """Options for creating constructs.

        :param node_factory: A factory for attaching ``Node``s to the construct. Default: - the default ``Node`` is associated
        """
        self._values = {
        }
        if node_factory is not None: self._values["node_factory"] = node_factory

    @builtins.property
    def node_factory(self) -> typing.Optional["INodeFactory"]:
        """A factory for attaching ``Node``s to the construct.

        default
        :default: - the default ``Node`` is associated
        """
        return self._values.get('node_factory')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ConstructOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="constructs.ConstructOrder")
class ConstructOrder(enum.Enum):
    """In what order to return constructs."""
    PREORDER = "PREORDER"
    """Depth-first, pre-order."""
    POSTORDER = "POSTORDER"
    """Depth-first, post-order (leaf nodes first)."""

@jsii.data_type(jsii_type="constructs.Dependency", jsii_struct_bases=[], name_mapping={'source': 'source', 'target': 'target'})
class Dependency():
    def __init__(self, *, source: "IConstruct", target: "IConstruct"):
        """A single dependency.

        :param source: Source the dependency.
        :param target: Target of the dependency.
        """
        self._values = {
            'source': source,
            'target': target,
        }

    @builtins.property
    def source(self) -> "IConstruct":
        """Source the dependency."""
        return self._values.get('source')

    @builtins.property
    def target(self) -> "IConstruct":
        """Target of the dependency."""
        return self._values.get('target')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Dependency(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="constructs.EncodingOptions", jsii_struct_bases=[], name_mapping={'display_hint': 'displayHint'})
class EncodingOptions():
    def __init__(self, *, display_hint: typing.Optional[str]=None):
        """Properties to string encodings.

        :param display_hint: A hint for the Token's purpose when stringifying it. Default: - no display hint
        """
        self._values = {
        }
        if display_hint is not None: self._values["display_hint"] = display_hint

    @builtins.property
    def display_hint(self) -> typing.Optional[str]:
        """A hint for the Token's purpose when stringifying it.

        default
        :default: - no display hint
        """
        return self._values.get('display_hint')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'EncodingOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="constructs.IAnyProducer")
class IAnyProducer(jsii.compat.Protocol):
    """Interface for lazy untyped value producers."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IAnyProducerProxy

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Any:
        """Produce the value.

        :param context: -
        """
        ...


class _IAnyProducerProxy():
    """Interface for lazy untyped value producers."""
    __jsii_type__ = "constructs.IAnyProducer"
    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Any:
        """Produce the value.

        :param context: -
        """
        return jsii.invoke(self, "produce", [context])


@jsii.interface(jsii_type="constructs.IAspect")
class IAspect(jsii.compat.Protocol):
    """Represents an Aspect."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IAspectProxy

    @jsii.member(jsii_name="visit")
    def visit(self, node: "IConstruct") -> None:
        """All aspects can visit an IConstruct.

        :param node: -
        """
        ...


class _IAspectProxy():
    """Represents an Aspect."""
    __jsii_type__ = "constructs.IAspect"
    @jsii.member(jsii_name="visit")
    def visit(self, node: "IConstruct") -> None:
        """All aspects can visit an IConstruct.

        :param node: -
        """
        return jsii.invoke(self, "visit", [node])


@jsii.interface(jsii_type="constructs.IConstruct")
class IConstruct(jsii.compat.Protocol):
    """Represents a construct."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IConstructProxy

    pass

class _IConstructProxy():
    """Represents a construct."""
    __jsii_type__ = "constructs.IConstruct"
    pass

@jsii.implements(IConstruct)
class Construct(metaclass=jsii.JSIIMeta, jsii_type="constructs.Construct"):
    """Represents the building block of the construct graph.

    All constructs besides the root construct must be created within the scope of
    another construct.
    """
    def __init__(self, scope: "Construct", id: str, *, node_factory: typing.Optional["INodeFactory"]=None) -> None:
        """Creates a new construct node.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings. If the ID includes a path separator (``/``), then it will be replaced by double dash ``--``.
        :param node_factory: A factory for attaching ``Node``s to the construct. Default: - the default ``Node`` is associated
        """
        options = ConstructOptions(node_factory=node_factory)

        jsii.create(Construct, self, [scope, id, options])

    @jsii.member(jsii_name="onPrepare")
    def _on_prepare(self) -> None:
        """Perform final modifications before synthesis.

        This method can be implemented by derived constructs in order to perform
        final changes before synthesis. prepare() will be called after child
        constructs have been prepared.

        This is an advanced framework feature. Only use this if you
        understand the implications.
        """
        return jsii.invoke(self, "onPrepare", [])

    @jsii.member(jsii_name="onSynthesize")
    def _on_synthesize(self, session: "ISynthesisSession") -> None:
        """Allows this construct to emit artifacts into the cloud assembly during synthesis.

        This method is usually implemented by framework-level constructs such as ``Stack`` and ``Asset``
        as they participate in synthesizing the cloud assembly.

        :param session: The synthesis session.
        """
        return jsii.invoke(self, "onSynthesize", [session])

    @jsii.member(jsii_name="onValidate")
    def _on_validate(self) -> typing.List[str]:
        """Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        return
        :return: An array of validation error messages, or an empty array if there the construct is valid.
        """
        return jsii.invoke(self, "onValidate", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Returns a string representation of this construct."""
        return jsii.invoke(self, "toString", [])


@jsii.interface(jsii_type="constructs.IFragmentConcatenator")
class IFragmentConcatenator(jsii.compat.Protocol):
    """Function used to concatenate symbols in the target document language.

    Interface so it could potentially be exposed over jsii.

    stability
    :stability: experimental
    """
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IFragmentConcatenatorProxy

    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        """Join the fragment on the left and on the right.

        :param left: -
        :param right: -

        stability
        :stability: experimental
        """
        ...


class _IFragmentConcatenatorProxy():
    """Function used to concatenate symbols in the target document language.

    Interface so it could potentially be exposed over jsii.

    stability
    :stability: experimental
    """
    __jsii_type__ = "constructs.IFragmentConcatenator"
    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        """Join the fragment on the left and on the right.

        :param left: -
        :param right: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "join", [left, right])


@jsii.interface(jsii_type="constructs.IListProducer")
class IListProducer(jsii.compat.Protocol):
    """Interface for lazy list producers."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IListProducerProxy

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[typing.List[str]]:
        """Produce the list value.

        :param context: -
        """
        ...


class _IListProducerProxy():
    """Interface for lazy list producers."""
    __jsii_type__ = "constructs.IListProducer"
    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[typing.List[str]]:
        """Produce the list value.

        :param context: -
        """
        return jsii.invoke(self, "produce", [context])


@jsii.interface(jsii_type="constructs.INodeFactory")
class INodeFactory(jsii.compat.Protocol):
    """A factory for attaching ``Node``s to the construct."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _INodeFactoryProxy

    @jsii.member(jsii_name="createNode")
    def create_node(self, host: "Construct", scope: "IConstruct", id: str) -> "Node":
        """Returns a new ``Node`` associated with ``host``.

        :param host: the associated construct.
        :param scope: the construct's scope (parent).
        :param id: the construct id.
        """
        ...


class _INodeFactoryProxy():
    """A factory for attaching ``Node``s to the construct."""
    __jsii_type__ = "constructs.INodeFactory"
    @jsii.member(jsii_name="createNode")
    def create_node(self, host: "Construct", scope: "IConstruct", id: str) -> "Node":
        """Returns a new ``Node`` associated with ``host``.

        :param host: the associated construct.
        :param scope: the construct's scope (parent).
        :param id: the construct id.
        """
        return jsii.invoke(self, "createNode", [host, scope, id])


@jsii.interface(jsii_type="constructs.INumberProducer")
class INumberProducer(jsii.compat.Protocol):
    """Interface for lazy number producers."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _INumberProducerProxy

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[jsii.Number]:
        """Produce the number value.

        :param context: -
        """
        ...


class _INumberProducerProxy():
    """Interface for lazy number producers."""
    __jsii_type__ = "constructs.INumberProducer"
    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[jsii.Number]:
        """Produce the number value.

        :param context: -
        """
        return jsii.invoke(self, "produce", [context])


@jsii.interface(jsii_type="constructs.IPostProcessor")
class IPostProcessor(jsii.compat.Protocol):
    """A Token that can post-process the complete resolved value, after resolve() has recursed over it."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IPostProcessorProxy

    @jsii.member(jsii_name="postProcess")
    def post_process(self, input: typing.Any, context: "IResolveContext") -> typing.Any:
        """Process the completely resolved value, after full recursion/resolution has happened.

        :param input: -
        :param context: -
        """
        ...


class _IPostProcessorProxy():
    """A Token that can post-process the complete resolved value, after resolve() has recursed over it."""
    __jsii_type__ = "constructs.IPostProcessor"
    @jsii.member(jsii_name="postProcess")
    def post_process(self, input: typing.Any, context: "IResolveContext") -> typing.Any:
        """Process the completely resolved value, after full recursion/resolution has happened.

        :param input: -
        :param context: -
        """
        return jsii.invoke(self, "postProcess", [input, context])


@jsii.interface(jsii_type="constructs.IResolvable")
class IResolvable(jsii.compat.Protocol):
    """Interface for values that can be resolvable later.

    Tokens are special objects that participate in synthesis.
    """
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IResolvableProxy

    @builtins.property
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[str]:
        """The creation stack of this resolvable which will be appended to errors thrown during resolution.

        If this returns an empty array the stack will not be attached.
        """
        ...

    @jsii.member(jsii_name="resolve")
    def resolve(self, context: "IResolveContext") -> typing.Any:
        """Produce the Token's value at resolution time.

        :param context: -
        """
        ...

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Return a string representation of this resolvable object.

        Returns a reversible string representation.
        """
        ...


class _IResolvableProxy():
    """Interface for values that can be resolvable later.

    Tokens are special objects that participate in synthesis.
    """
    __jsii_type__ = "constructs.IResolvable"
    @builtins.property
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[str]:
        """The creation stack of this resolvable which will be appended to errors thrown during resolution.

        If this returns an empty array the stack will not be attached.
        """
        return jsii.get(self, "creationStack")

    @jsii.member(jsii_name="resolve")
    def resolve(self, context: "IResolveContext") -> typing.Any:
        """Produce the Token's value at resolution time.

        :param context: -
        """
        return jsii.invoke(self, "resolve", [context])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Return a string representation of this resolvable object.

        Returns a reversible string representation.
        """
        return jsii.invoke(self, "toString", [])


@jsii.interface(jsii_type="constructs.IResolveContext")
class IResolveContext(jsii.compat.Protocol):
    """Current resolution context for tokens."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IResolveContextProxy

    @builtins.property
    @jsii.member(jsii_name="preparing")
    def preparing(self) -> bool:
        """True when we are still preparing, false if we're rendering the final output."""
        ...

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> "IConstruct":
        """The scope from which resolution has been initiated."""
        ...

    @jsii.member(jsii_name="registerPostProcessor")
    def register_post_processor(self, post_processor: "IPostProcessor") -> None:
        """Use this postprocessor after the entire token structure has been resolved.

        :param post_processor: -
        """
        ...

    @jsii.member(jsii_name="resolve")
    def resolve(self, x: typing.Any) -> typing.Any:
        """Resolve an inner object.

        :param x: -
        """
        ...


class _IResolveContextProxy():
    """Current resolution context for tokens."""
    __jsii_type__ = "constructs.IResolveContext"
    @builtins.property
    @jsii.member(jsii_name="preparing")
    def preparing(self) -> bool:
        """True when we are still preparing, false if we're rendering the final output."""
        return jsii.get(self, "preparing")

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> "IConstruct":
        """The scope from which resolution has been initiated."""
        return jsii.get(self, "scope")

    @jsii.member(jsii_name="registerPostProcessor")
    def register_post_processor(self, post_processor: "IPostProcessor") -> None:
        """Use this postprocessor after the entire token structure has been resolved.

        :param post_processor: -
        """
        return jsii.invoke(self, "registerPostProcessor", [post_processor])

    @jsii.member(jsii_name="resolve")
    def resolve(self, x: typing.Any) -> typing.Any:
        """Resolve an inner object.

        :param x: -
        """
        return jsii.invoke(self, "resolve", [x])


@jsii.interface(jsii_type="constructs.IStringProducer")
class IStringProducer(jsii.compat.Protocol):
    """Interface for lazy string producers."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IStringProducerProxy

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[str]:
        """Produce the string value.

        :param context: -
        """
        ...


class _IStringProducerProxy():
    """Interface for lazy string producers."""
    __jsii_type__ = "constructs.IStringProducer"
    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[str]:
        """Produce the string value.

        :param context: -
        """
        return jsii.invoke(self, "produce", [context])


@jsii.interface(jsii_type="constructs.ISynthesisSession")
class ISynthesisSession(jsii.compat.Protocol):
    """Represents a single session of synthesis.

    Passed into ``construct.onSynthesize()`` methods.
    """
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ISynthesisSessionProxy

    @builtins.property
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> str:
        """The output directory for this synthesis session."""
        ...


class _ISynthesisSessionProxy():
    """Represents a single session of synthesis.

    Passed into ``construct.onSynthesize()`` methods.
    """
    __jsii_type__ = "constructs.ISynthesisSession"
    @builtins.property
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> str:
        """The output directory for this synthesis session."""
        return jsii.get(self, "outdir")


@jsii.interface(jsii_type="constructs.ITokenMapper")
class ITokenMapper(jsii.compat.Protocol):
    """Interface to apply operation to tokens in a string.

    Interface so it can be exported via jsii.
    """
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ITokenMapperProxy

    @jsii.member(jsii_name="mapToken")
    def map_token(self, t: "IResolvable") -> typing.Any:
        """Replace a single token.

        :param t: -
        """
        ...


class _ITokenMapperProxy():
    """Interface to apply operation to tokens in a string.

    Interface so it can be exported via jsii.
    """
    __jsii_type__ = "constructs.ITokenMapper"
    @jsii.member(jsii_name="mapToken")
    def map_token(self, t: "IResolvable") -> typing.Any:
        """Replace a single token.

        :param t: -
        """
        return jsii.invoke(self, "mapToken", [t])


@jsii.interface(jsii_type="constructs.ITokenResolver")
class ITokenResolver(jsii.compat.Protocol):
    """How to resolve tokens."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ITokenResolverProxy

    @jsii.member(jsii_name="resolveList")
    def resolve_list(self, l: typing.List[str], context: "IResolveContext") -> typing.Any:
        """Resolve a tokenized list.

        :param l: -
        :param context: -
        """
        ...

    @jsii.member(jsii_name="resolveString")
    def resolve_string(self, s: "TokenizedStringFragments", context: "IResolveContext") -> typing.Any:
        """Resolve a string with at least one stringified token in it.

        (May use concatenation)

        :param s: -
        :param context: -
        """
        ...

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(self, t: "IResolvable", context: "IResolveContext", post_processor: "IPostProcessor") -> typing.Any:
        """Resolve a single token.

        :param t: -
        :param context: -
        :param post_processor: -
        """
        ...


class _ITokenResolverProxy():
    """How to resolve tokens."""
    __jsii_type__ = "constructs.ITokenResolver"
    @jsii.member(jsii_name="resolveList")
    def resolve_list(self, l: typing.List[str], context: "IResolveContext") -> typing.Any:
        """Resolve a tokenized list.

        :param l: -
        :param context: -
        """
        return jsii.invoke(self, "resolveList", [l, context])

    @jsii.member(jsii_name="resolveString")
    def resolve_string(self, s: "TokenizedStringFragments", context: "IResolveContext") -> typing.Any:
        """Resolve a string with at least one stringified token in it.

        (May use concatenation)

        :param s: -
        :param context: -
        """
        return jsii.invoke(self, "resolveString", [s, context])

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(self, t: "IResolvable", context: "IResolveContext", post_processor: "IPostProcessor") -> typing.Any:
        """Resolve a single token.

        :param t: -
        :param context: -
        :param post_processor: -
        """
        return jsii.invoke(self, "resolveToken", [t, context, post_processor])


@jsii.implements(ITokenResolver)
class DefaultTokenResolver(metaclass=jsii.JSIIMeta, jsii_type="constructs.DefaultTokenResolver"):
    """Default resolver implementation.

    stability
    :stability: experimental
    """
    def __init__(self, concat: "IFragmentConcatenator") -> None:
        """
        :param concat: -

        stability
        :stability: experimental
        """
        jsii.create(DefaultTokenResolver, self, [concat])

    @jsii.member(jsii_name="resolveList")
    def resolve_list(self, xs: typing.List[str], context: "IResolveContext") -> typing.Any:
        """Resolve a tokenized list.

        :param xs: -
        :param context: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "resolveList", [xs, context])

    @jsii.member(jsii_name="resolveString")
    def resolve_string(self, fragments: "TokenizedStringFragments", context: "IResolveContext") -> typing.Any:
        """Resolve string fragments to Tokens.

        :param fragments: -
        :param context: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "resolveString", [fragments, context])

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(self, t: "IResolvable", context: "IResolveContext", post_processor: "IPostProcessor") -> typing.Any:
        """Default Token resolution.

        Resolve the Token, recurse into whatever it returns,
        then finally post-process it.

        :param t: -
        :param context: -
        :param post_processor: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "resolveToken", [t, context, post_processor])


class Lazy(metaclass=jsii.JSIIMeta, jsii_type="constructs.Lazy"):
    """Lazily produce a value.

    Can be used to return a string, list or numeric value whose actual value
    will only be calculated later, during synthesis.
    """
    @jsii.member(jsii_name="anyValue")
    @builtins.classmethod
    def any_value(cls, producer: "IAnyProducer", *, display_hint: typing.Optional[str]=None, omit_empty_array: typing.Optional[bool]=None) -> "IResolvable":
        """Produces a lazy token from an untyped value.

        :param producer: The lazy producer.
        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty_array: If the produced value is an array and it is empty, return 'undefined' instead. Default: false
        """
        options = LazyAnyValueOptions(display_hint=display_hint, omit_empty_array=omit_empty_array)

        return jsii.sinvoke(cls, "anyValue", [producer, options])

    @jsii.member(jsii_name="listValue")
    @builtins.classmethod
    def list_value(cls, producer: "IListProducer", *, display_hint: typing.Optional[str]=None, omit_empty: typing.Optional[bool]=None) -> typing.List[str]:
        """Returns a list-ified token for a lazy value.

        :param producer: The producer.
        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty: If the produced list is empty, return 'undefined' instead. Default: false
        """
        options = LazyListValueOptions(display_hint=display_hint, omit_empty=omit_empty)

        return jsii.sinvoke(cls, "listValue", [producer, options])

    @jsii.member(jsii_name="numberValue")
    @builtins.classmethod
    def number_value(cls, producer: "INumberProducer") -> jsii.Number:
        """Returns a numberified token for a lazy value.

        :param producer: The producer.
        """
        return jsii.sinvoke(cls, "numberValue", [producer])

    @jsii.member(jsii_name="stringValue")
    @builtins.classmethod
    def string_value(cls, producer: "IStringProducer", *, display_hint: typing.Optional[str]=None) -> str:
        """Returns a stringified token for a lazy value.

        :param producer: The producer.
        :param display_hint: Use the given name as a display hint. Default: - No hint
        """
        options = LazyStringValueOptions(display_hint=display_hint)

        return jsii.sinvoke(cls, "stringValue", [producer, options])


@jsii.data_type(jsii_type="constructs.LazyAnyValueOptions", jsii_struct_bases=[], name_mapping={'display_hint': 'displayHint', 'omit_empty_array': 'omitEmptyArray'})
class LazyAnyValueOptions():
    def __init__(self, *, display_hint: typing.Optional[str]=None, omit_empty_array: typing.Optional[bool]=None):
        """Options for creating lazy untyped tokens.

        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty_array: If the produced value is an array and it is empty, return 'undefined' instead. Default: false
        """
        self._values = {
        }
        if display_hint is not None: self._values["display_hint"] = display_hint
        if omit_empty_array is not None: self._values["omit_empty_array"] = omit_empty_array

    @builtins.property
    def display_hint(self) -> typing.Optional[str]:
        """Use the given name as a display hint.

        default
        :default: - No hint
        """
        return self._values.get('display_hint')

    @builtins.property
    def omit_empty_array(self) -> typing.Optional[bool]:
        """If the produced value is an array and it is empty, return 'undefined' instead.

        default
        :default: false
        """
        return self._values.get('omit_empty_array')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'LazyAnyValueOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="constructs.LazyListValueOptions", jsii_struct_bases=[], name_mapping={'display_hint': 'displayHint', 'omit_empty': 'omitEmpty'})
class LazyListValueOptions():
    def __init__(self, *, display_hint: typing.Optional[str]=None, omit_empty: typing.Optional[bool]=None):
        """Options for creating a lazy list token.

        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty: If the produced list is empty, return 'undefined' instead. Default: false
        """
        self._values = {
        }
        if display_hint is not None: self._values["display_hint"] = display_hint
        if omit_empty is not None: self._values["omit_empty"] = omit_empty

    @builtins.property
    def display_hint(self) -> typing.Optional[str]:
        """Use the given name as a display hint.

        default
        :default: - No hint
        """
        return self._values.get('display_hint')

    @builtins.property
    def omit_empty(self) -> typing.Optional[bool]:
        """If the produced list is empty, return 'undefined' instead.

        default
        :default: false
        """
        return self._values.get('omit_empty')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'LazyListValueOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="constructs.LazyStringValueOptions", jsii_struct_bases=[], name_mapping={'display_hint': 'displayHint'})
class LazyStringValueOptions():
    def __init__(self, *, display_hint: typing.Optional[str]=None):
        """Options for creating a lazy string token.

        :param display_hint: Use the given name as a display hint. Default: - No hint
        """
        self._values = {
        }
        if display_hint is not None: self._values["display_hint"] = display_hint

    @builtins.property
    def display_hint(self) -> typing.Optional[str]:
        """Use the given name as a display hint.

        default
        :default: - No hint
        """
        return self._values.get('display_hint')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'LazyStringValueOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="constructs.MetadataEntry", jsii_struct_bases=[], name_mapping={'data': 'data', 'type': 'type', 'trace': 'trace'})
class MetadataEntry():
    def __init__(self, *, data: typing.Any, type: str, trace: typing.Optional[typing.List[str]]=None):
        """An entry in the construct metadata table.

        :param data: The data.
        :param type: The metadata entry type.
        :param trace: Stack trace. Can be omitted by setting the context key ``ConstructMetadata.DISABLE_STACK_TRACE_IN_METADATA`` to 1. Default: - no trace information
        """
        self._values = {
            'data': data,
            'type': type,
        }
        if trace is not None: self._values["trace"] = trace

    @builtins.property
    def data(self) -> typing.Any:
        """The data."""
        return self._values.get('data')

    @builtins.property
    def type(self) -> str:
        """The metadata entry type."""
        return self._values.get('type')

    @builtins.property
    def trace(self) -> typing.Optional[typing.List[str]]:
        """Stack trace.

        Can be omitted by setting the context key
        ``ConstructMetadata.DISABLE_STACK_TRACE_IN_METADATA`` to 1.

        default
        :default: - no trace information
        """
        return self._values.get('trace')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MetadataEntry(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Node(metaclass=jsii.JSIIMeta, jsii_type="constructs.Node"):
    """Represents the construct node in the scope tree."""
    def __init__(self, host: "Construct", scope: "IConstruct", id: str) -> None:
        """
        :param host: -
        :param scope: -
        :param id: -
        """
        jsii.create(Node, self, [host, scope, id])

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, construct: "IConstruct") -> "Node":
        """Returns the node associated with a construct.

        :param construct: the construct.
        """
        return jsii.sinvoke(cls, "of", [construct])

    @jsii.member(jsii_name="addDependency")
    def add_dependency(self, *dependencies: "IConstruct") -> None:
        """Add an ordering dependency on another Construct.

        All constructs in the dependency's scope will be deployed before any
        construct in this construct's scope.

        :param dependencies: -
        """
        return jsii.invoke(self, "addDependency", [*dependencies])

    @jsii.member(jsii_name="addError")
    def add_error(self, message: str) -> None:
        """Adds an { "error":  } metadata entry to this construct.

        The toolkit will fail synthesis when errors are reported.

        :param message: The error message.
        """
        return jsii.invoke(self, "addError", [message])

    @jsii.member(jsii_name="addInfo")
    def add_info(self, message: str) -> None:
        """Adds a { "info":  } metadata entry to this construct.

        The toolkit will display the info message when apps are synthesized.

        :param message: The info message.
        """
        return jsii.invoke(self, "addInfo", [message])

    @jsii.member(jsii_name="addMetadata")
    def add_metadata(self, type: str, data: typing.Any, from_function: typing.Any=None) -> None:
        """Adds a metadata entry to this construct.

        Entries are arbitrary values and will also include a stack trace to allow tracing back to
        the code location for when the entry was added. It can be used, for example, to include source
        mapping in CloudFormation templates to improve diagnostics.

        :param type: a string denoting the type of metadata.
        :param data: the value of the metadata (can be a Token). If null/undefined, metadata will not be added.
        :param from_function: a function under which to restrict the metadata entry's stack trace (defaults to this.addMetadata).
        """
        return jsii.invoke(self, "addMetadata", [type, data, from_function])

    @jsii.member(jsii_name="addWarning")
    def add_warning(self, message: str) -> None:
        """Adds a { "warning":  } metadata entry to this construct.

        The toolkit will display the warning when an app is synthesized, or fail
        if run in --strict mode.

        :param message: The warning message.
        """
        return jsii.invoke(self, "addWarning", [message])

    @jsii.member(jsii_name="applyAspect")
    def apply_aspect(self, aspect: "IAspect") -> None:
        """Applies the aspect to this Constructs node.

        :param aspect: -
        """
        return jsii.invoke(self, "applyAspect", [aspect])

    @jsii.member(jsii_name="findAll")
    def find_all(self, order: typing.Optional["ConstructOrder"]=None) -> typing.List["IConstruct"]:
        """Return this construct and all of its children in the given order.

        :param order: -
        """
        return jsii.invoke(self, "findAll", [order])

    @jsii.member(jsii_name="findChild")
    def find_child(self, id: str) -> "IConstruct":
        """Return a direct child by id.

        Throws an error if the child is not found.

        :param id: Identifier of direct child.

        return
        :return: Child with the given id.
        """
        return jsii.invoke(self, "findChild", [id])

    @jsii.member(jsii_name="prepare")
    def prepare(self) -> None:
        """Invokes "prepare" on all constructs (depth-first, post-order) in the tree under ``node``."""
        return jsii.invoke(self, "prepare", [])

    @jsii.member(jsii_name="setContext")
    def set_context(self, key: str, value: typing.Any) -> None:
        """This can be used to set contextual values.

        Context must be set before any children are added, since children may consult context info during construction.
        If the key already exists, it will be overridden.

        :param key: The context key.
        :param value: The context value.
        """
        return jsii.invoke(self, "setContext", [key, value])

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, *, outdir: str, session_context: typing.Optional[typing.Mapping[str,typing.Any]]=None, skip_validation: typing.Optional[bool]=None) -> None:
        """Synthesizes a CloudAssembly from a construct tree.

        :param outdir: The output directory into which to synthesize the cloud assembly. Default: - creates a temporary directory
        :param session_context: Additional context passed into the synthesis session object when ``construct.synth`` is called. Default: - no additional context is passed to ``onSynthesize``
        :param skip_validation: Whether synthesis should skip the validation phase. Default: false
        """
        options = SynthesisOptions(outdir=outdir, session_context=session_context, skip_validation=skip_validation)

        return jsii.invoke(self, "synthesize", [options])

    @jsii.member(jsii_name="tryFindChild")
    def try_find_child(self, id: str) -> typing.Optional["IConstruct"]:
        """Return a direct child by id, or undefined.

        :param id: Identifier of direct child.

        return
        :return: the child if found, or undefined
        """
        return jsii.invoke(self, "tryFindChild", [id])

    @jsii.member(jsii_name="tryGetContext")
    def try_get_context(self, key: str) -> typing.Any:
        """Retrieves a value from tree context.

        Context is usually initialized at the root, but can be overridden at any point in the tree.

        :param key: The context key.

        return
        :return: The context value or ``undefined`` if there is no context value for thie key.
        """
        return jsii.invoke(self, "tryGetContext", [key])

    @jsii.member(jsii_name="tryRemoveChild")
    def try_remove_child(self, child_name: str) -> bool:
        """Remove the child with the given name, if present.

        :param child_name: -

        return
        :return: Whether a child with the given name was deleted.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "tryRemoveChild", [child_name])

    @jsii.member(jsii_name="validate")
    def validate(self) -> typing.List["ValidationError"]:
        """Invokes "validate" on all constructs in the tree (depth-first, pre-order) and returns the list of all errors.

        An empty list indicates that there are no errors.
        """
        return jsii.invoke(self, "validate", [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PATH_SEP")
    def PATH_SEP(cls) -> str:
        """Separator used to delimit construct path components."""
        return jsii.sget(cls, "PATH_SEP")

    @builtins.property
    @jsii.member(jsii_name="children")
    def children(self) -> typing.List["IConstruct"]:
        """All direct children of this construct."""
        return jsii.get(self, "children")

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["Dependency"]:
        """Return all dependencies registered on this node or any of its children."""
        return jsii.get(self, "dependencies")

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> str:
        """The id of this construct within the current scope.

        This is a a scope-unique id. To obtain an app-unique id for this construct, use ``uniqueId``.
        """
        return jsii.get(self, "id")

    @builtins.property
    @jsii.member(jsii_name="locked")
    def locked(self) -> bool:
        """Returns true if this construct or the scopes in which it is defined are locked."""
        return jsii.get(self, "locked")

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.List["MetadataEntry"]:
        """An immutable array of metadata objects associated with this construct.

        This can be used, for example, to implement support for deprecation notices, source mapping, etc.
        """
        return jsii.get(self, "metadata")

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> str:
        """The full, absolute path of this construct in the tree.

        Components are separated by '/'.
        """
        return jsii.get(self, "path")

    @builtins.property
    @jsii.member(jsii_name="root")
    def root(self) -> "IConstruct":
        """Returns the root of the construct tree.

        return
        :return: The root of the construct tree.
        """
        return jsii.get(self, "root")

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List["IConstruct"]:
        """All parent scopes of this construct.

        return
        :return:

        a list of parent scopes. The last element in the list will always
        be the current construct and the first element will be the root of the
        tree.
        """
        return jsii.get(self, "scopes")

    @builtins.property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> str:
        """A tree-global unique alphanumeric identifier for this construct.

        Includes all components of the tree.
        """
        return jsii.get(self, "uniqueId")

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> typing.Optional["IConstruct"]:
        """Returns the scope in which this construct is defined.

        The value is ``undefined`` at the root of the construct scope tree.
        """
        return jsii.get(self, "scope")

    @builtins.property
    @jsii.member(jsii_name="defaultChild")
    def default_child(self) -> typing.Optional["IConstruct"]:
        """Returns the child construct that has the id ``Default`` or ``Resource"``.

        This is usually the construct that provides the bulk of the underlying functionality.
        Useful for modifications of the underlying construct that are not available at the higher levels.
        Override the defaultChild property.

        This should only be used in the cases where the correct
        default child is not named 'Resource' or 'Default' as it
        should be.

        If you set this to undefined, the default behavior of finding
        the child named 'Resource' or 'Default' will be used.

        return
        :return: a construct or undefined if there is no default child

        throws:
        :throws:: if there is more than one child
        """
        return jsii.get(self, "defaultChild")

    @default_child.setter
    def default_child(self, value: typing.Optional["IConstruct"]):
        jsii.set(self, "defaultChild", value)


@jsii.data_type(jsii_type="constructs.ResolveOptions", jsii_struct_bases=[], name_mapping={'resolver': 'resolver', 'scope': 'scope', 'preparing': 'preparing'})
class ResolveOptions():
    def __init__(self, *, resolver: "ITokenResolver", scope: "IConstruct", preparing: typing.Optional[bool]=None):
        """Options to the resolve() operation.

        NOT the same as the ResolveContext; ResolveContext is exposed to Token
        implementors and resolution hooks, whereas this struct is just to bundle
        a number of things that would otherwise be arguments to resolve() in a
        readable way.

        :param resolver: The resolver to apply to any resolvable tokens found.
        :param scope: The scope from which resolution is performed.
        :param preparing: Whether the resolution is being executed during the prepare phase or not. Default: false
        """
        self._values = {
            'resolver': resolver,
            'scope': scope,
        }
        if preparing is not None: self._values["preparing"] = preparing

    @builtins.property
    def resolver(self) -> "ITokenResolver":
        """The resolver to apply to any resolvable tokens found."""
        return self._values.get('resolver')

    @builtins.property
    def scope(self) -> "IConstruct":
        """The scope from which resolution is performed."""
        return self._values.get('scope')

    @builtins.property
    def preparing(self) -> typing.Optional[bool]:
        """Whether the resolution is being executed during the prepare phase or not.

        default
        :default: false
        """
        return self._values.get('preparing')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ResolveOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IFragmentConcatenator)
class StringConcat(metaclass=jsii.JSIIMeta, jsii_type="constructs.StringConcat"):
    """Converts all fragments to strings and concats those.

    Drops 'undefined's.
    """
    def __init__(self) -> None:
        jsii.create(StringConcat, self, [])

    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        """Join the fragment on the left and on the right.

        :param left: -
        :param right: -
        """
        return jsii.invoke(self, "join", [left, right])


@jsii.data_type(jsii_type="constructs.SynthesisOptions", jsii_struct_bases=[], name_mapping={'outdir': 'outdir', 'session_context': 'sessionContext', 'skip_validation': 'skipValidation'})
class SynthesisOptions():
    def __init__(self, *, outdir: str, session_context: typing.Optional[typing.Mapping[str,typing.Any]]=None, skip_validation: typing.Optional[bool]=None):
        """Options for synthesis.

        :param outdir: The output directory into which to synthesize the cloud assembly. Default: - creates a temporary directory
        :param session_context: Additional context passed into the synthesis session object when ``construct.synth`` is called. Default: - no additional context is passed to ``onSynthesize``
        :param skip_validation: Whether synthesis should skip the validation phase. Default: false
        """
        self._values = {
            'outdir': outdir,
        }
        if session_context is not None: self._values["session_context"] = session_context
        if skip_validation is not None: self._values["skip_validation"] = skip_validation

    @builtins.property
    def outdir(self) -> str:
        """The output directory into which to synthesize the cloud assembly.

        default
        :default: - creates a temporary directory
        """
        return self._values.get('outdir')

    @builtins.property
    def session_context(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """Additional context passed into the synthesis session object when ``construct.synth`` is called.

        default
        :default: - no additional context is passed to ``onSynthesize``
        """
        return self._values.get('session_context')

    @builtins.property
    def skip_validation(self) -> typing.Optional[bool]:
        """Whether synthesis should skip the validation phase.

        default
        :default: false
        """
        return self._values.get('skip_validation')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SynthesisOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Token(metaclass=jsii.JSIIMeta, jsii_type="constructs.Token"):
    """Represents a special or lazily-evaluated value.

    Can be used to delay evaluation of a certain value in case, for example,
    that it requires some context or late-bound data. Can also be used to
    mark values that need special processing at document rendering time.

    Tokens can be embedded into strings while retaining their original
    semantics.
    """
    @jsii.member(jsii_name="asAny")
    @builtins.classmethod
    def as_any(cls, value: typing.Any) -> "IResolvable":
        """Return a resolvable representation of the given value.

        :param value: -
        """
        return jsii.sinvoke(cls, "asAny", [value])

    @jsii.member(jsii_name="asList")
    @builtins.classmethod
    def as_list(cls, value: typing.Any, *, display_hint: typing.Optional[str]=None) -> typing.List[str]:
        """Return a reversible list representation of this token.

        :param value: -
        :param display_hint: A hint for the Token's purpose when stringifying it. Default: - no display hint
        """
        options = EncodingOptions(display_hint=display_hint)

        return jsii.sinvoke(cls, "asList", [value, options])

    @jsii.member(jsii_name="asNumber")
    @builtins.classmethod
    def as_number(cls, value: typing.Any) -> jsii.Number:
        """Return a reversible number representation of this token.

        :param value: -
        """
        return jsii.sinvoke(cls, "asNumber", [value])

    @jsii.member(jsii_name="asString")
    @builtins.classmethod
    def as_string(cls, value: typing.Any, *, display_hint: typing.Optional[str]=None) -> str:
        """Return a reversible string representation of this token.

        If the Token is initialized with a literal, the stringified value of the
        literal is returned. Otherwise, a special quoted string representation
        of the Token is returned that can be embedded into other strings.

        Strings with quoted Tokens in them can be restored back into
        complex values with the Tokens restored by calling ``resolve()``
        on the string.

        :param value: -
        :param display_hint: A hint for the Token's purpose when stringifying it. Default: - no display hint
        """
        options = EncodingOptions(display_hint=display_hint)

        return jsii.sinvoke(cls, "asString", [value, options])

    @jsii.member(jsii_name="isUnresolved")
    @builtins.classmethod
    def is_unresolved(cls, obj: typing.Any) -> bool:
        """Returns true if obj represents an unresolved value.

        One of these must be true:

        - ``obj`` is an IResolvable
        - ``obj`` is a string containing at least one encoded ``IResolvable``
        - ``obj`` is either an encoded number or list

        This does NOT recurse into lists or objects to see if they
        containing resolvables.

        :param obj: The object to test.
        """
        return jsii.sinvoke(cls, "isUnresolved", [obj])


class Tokenization(metaclass=jsii.JSIIMeta, jsii_type="constructs.Tokenization"):
    """Less oft-needed functions to manipulate Tokens."""
    @jsii.member(jsii_name="isResolvable")
    @builtins.classmethod
    def is_resolvable(cls, obj: typing.Any) -> bool:
        """Return whether the given object is an IResolvable object.

        This is different from Token.isUnresolved() which will also check for
        encoded Tokens, whereas this method will only do a type check on the given
        object.

        :param obj: -
        """
        return jsii.sinvoke(cls, "isResolvable", [obj])

    @jsii.member(jsii_name="resolve")
    @builtins.classmethod
    def resolve(cls, obj: typing.Any, *, resolver: "ITokenResolver", scope: "IConstruct", preparing: typing.Optional[bool]=None) -> typing.Any:
        """Resolves an object by evaluating all tokens and removing any undefined or empty objects or arrays.

        Values can only be primitives, arrays or tokens. Other objects (i.e. with methods) will be rejected.

        :param obj: The object to resolve.
        :param resolver: The resolver to apply to any resolvable tokens found.
        :param scope: The scope from which resolution is performed.
        :param preparing: Whether the resolution is being executed during the prepare phase or not. Default: false
        """
        options = ResolveOptions(resolver=resolver, scope=scope, preparing=preparing)

        return jsii.sinvoke(cls, "resolve", [obj, options])

    @jsii.member(jsii_name="reverseList")
    @builtins.classmethod
    def reverse_list(cls, l: typing.List[str]) -> typing.Optional["IResolvable"]:
        """Un-encode a Tokenized value from a list.

        :param l: -
        """
        return jsii.sinvoke(cls, "reverseList", [l])

    @jsii.member(jsii_name="reverseNumber")
    @builtins.classmethod
    def reverse_number(cls, n: jsii.Number) -> typing.Optional["IResolvable"]:
        """Un-encode a Tokenized value from a number.

        :param n: -
        """
        return jsii.sinvoke(cls, "reverseNumber", [n])

    @jsii.member(jsii_name="reverseString")
    @builtins.classmethod
    def reverse_string(cls, s: str) -> "TokenizedStringFragments":
        """Un-encode a string potentially containing encoded tokens.

        :param s: -
        """
        return jsii.sinvoke(cls, "reverseString", [s])

    @jsii.member(jsii_name="stringifyNumber")
    @builtins.classmethod
    def stringify_number(cls, x: jsii.Number) -> str:
        """Stringify a number directly or lazily if it's a Token.

        If it is an object (i.e., { Ref: 'SomeLogicalId' }), return it as-is.

        :param x: -
        """
        return jsii.sinvoke(cls, "stringifyNumber", [x])


class TokenizedStringFragments(metaclass=jsii.JSIIMeta, jsii_type="constructs.TokenizedStringFragments"):
    """Fragments of a concatenated string containing stringified Tokens.

    stability
    :stability: experimental
    """
    def __init__(self) -> None:
        jsii.create(TokenizedStringFragments, self, [])

    @jsii.member(jsii_name="addIntrinsic")
    def add_intrinsic(self, value: typing.Any) -> None:
        """Adds an intrinsic fragment.

        :param value: the intrinsic value to add.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addIntrinsic", [value])

    @jsii.member(jsii_name="addLiteral")
    def add_literal(self, lit: typing.Any) -> None:
        """Adds a literal fragment.

        :param lit: the literal to add.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addLiteral", [lit])

    @jsii.member(jsii_name="addToken")
    def add_token(self, token: "IResolvable") -> None:
        """Adds a token fragment.

        :param token: the token to add.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addToken", [token])

    @jsii.member(jsii_name="join")
    def join(self, concat: "IFragmentConcatenator") -> typing.Any:
        """Combine the string fragments using the given joiner.

        If there are any

        :param concat: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "join", [concat])

    @jsii.member(jsii_name="mapTokens")
    def map_tokens(self, mapper: "ITokenMapper") -> "TokenizedStringFragments":
        """Apply a transformation function to all tokens in the string.

        :param mapper: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "mapTokens", [mapper])

    @builtins.property
    @jsii.member(jsii_name="firstValue")
    def first_value(self) -> typing.Any:
        """Returns the first value.

        stability
        :stability: experimental
        """
        return jsii.get(self, "firstValue")

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        """Returns the number of fragments.

        stability
        :stability: experimental
        """
        return jsii.get(self, "length")

    @builtins.property
    @jsii.member(jsii_name="tokens")
    def tokens(self) -> typing.List["IResolvable"]:
        """Return all Tokens from this string.

        stability
        :stability: experimental
        """
        return jsii.get(self, "tokens")

    @builtins.property
    @jsii.member(jsii_name="firstToken")
    def first_token(self) -> typing.Optional["IResolvable"]:
        """Returns the first token.

        stability
        :stability: experimental
        """
        return jsii.get(self, "firstToken")


@jsii.data_type(jsii_type="constructs.ValidationError", jsii_struct_bases=[], name_mapping={'message': 'message', 'source': 'source'})
class ValidationError():
    def __init__(self, *, message: str, source: "Construct"):
        """An error returned during the validation phase.

        :param message: The error message.
        :param source: The construct which emitted the error.
        """
        self._values = {
            'message': message,
            'source': source,
        }

    @builtins.property
    def message(self) -> str:
        """The error message."""
        return self._values.get('message')

    @builtins.property
    def source(self) -> "Construct":
        """The construct which emitted the error."""
        return self._values.get('source')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ValidationError(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["Construct", "ConstructMetadata", "ConstructOptions", "ConstructOrder", "DefaultTokenResolver", "Dependency", "EncodingOptions", "IAnyProducer", "IAspect", "IConstruct", "IFragmentConcatenator", "IListProducer", "INodeFactory", "INumberProducer", "IPostProcessor", "IResolvable", "IResolveContext", "IStringProducer", "ISynthesisSession", "ITokenMapper", "ITokenResolver", "Lazy", "LazyAnyValueOptions", "LazyListValueOptions", "LazyStringValueOptions", "MetadataEntry", "Node", "ResolveOptions", "StringConcat", "SynthesisOptions", "Token", "Tokenization", "TokenizedStringFragments", "ValidationError", "__jsii_assembly__"]

publication.publish()
